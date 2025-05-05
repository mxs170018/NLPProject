# MXS170018
# MANUEL SALADO ALVARADO

from kafka import KafkaConsumer
import json
import sys
import requests
from datetime import datetime, timedelta
import random 
import math

from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QTextEdit
)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QPalette, QColor, QFont, QPixmap
from openai import OpenAI
import wikipediaapi
import os
os.environ["QT_QPA_PLATFORM"] = "wayland"
client = OpenAI(
    api_key="SECRET"
wiki = wikipediaapi.Wikipedia(
    user_agent='MyProjectName (merlin@example.com)',
    language="en"
    )
# response = client.responses.create(
#     model="gpt-4.1-nano",
#     input="tell me a joke about ducks"
# )

# print(response.output_text)
class InfoFetcher(QThread):
    finished = pyqtSignal(str)

    def __init__(self, topic):
        super().__init__()
        self.topic = topic

    def run(self):
        try:
            summary = self.get_wikipedia_summary(self.topic)
            news = self.get_recent_news(self.topic)
            response = self.query_openai(summary, news, self.topic)
            self.finished.emit(response)
        except Exception as e:
            self.finished.emit(f"Error: {e}")

    def get_wikipedia_summary(self, title):
        page = wiki.page(title)
        return page.summary if page.exists() else "No Wikipedia info found."

    def get_recent_news(self, query):
        url = f"https://newsapi.org/v2/everything?q={query}&pageSize=3&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
        resp = requests.get(url)
        articles = resp.json().get("articles", [])
        return "\n\n".join(f"{a['title']} - {a['description']}" for a in articles[:3])

    def query_openai(self, summary, news, subject):
        prompt = (
            f"Give me an overview of with an emphasis on recent news, don't be politically correct{subject}.\n\n"
            f"Background info (Named entity recognition was performed, assume we are talking about corporations or people):\n{summary}\n\n"
            f"Recent news:\n{news}\n\n"
            f"Summarize current events and bring up key facts of the background info if it helps contextualize(emphasis on current events, and be specific and include details from the articles)."
        )
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("COMET NEWS")
        self.resize(1300, 700)
        self.setStyleSheet("color: #B7410E;")
        # In MainWindow.__init__:
        self.response_cache = {}  # key = entity, value = (response_text, timestamp)
        self.cache_duration = timedelta(minutes=5)
        # Main layout
        main_widget = QWidget()
        main_widget.setStyleSheet("background-color: #ec7524;")
        main_layout = QHBoxLayout(main_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(main_widget)
        

        # ─── LEFT: BARCHART ───
        self.chart_label = QLabel()
        font = QFont("Courier", 15)
        font.setBold(True)
        self.chart_label.setFont(font)
        self.chart_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.chart_label.setMinimumWidth(400)
        self.chart_label.setStyleSheet("color: #114634;")
        # LEFT: chart panel with image underneath
        left_panel = QVBoxLayout()

        # Chart label
        self.chart_label = QLabel()
        font = QFont("Courier", 15)
        font.setBold(True)
        self.chart_label.setFont(font)
        self.chart_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.chart_label.setStyleSheet("color: #114634;")
        left_panel.addWidget(self.chart_label)

        # Spacer
        left_panel.addStretch()

        # Image label
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap("temoc.png").scaledToWidth(150))
        self.image_label.setAlignment(Qt.AlignCenter)  # optional: QLabel internal alignment

        # Center horizontally using an HBox layout
        image_row = QHBoxLayout()
        image_row.addStretch()
        image_row.addWidget(self.image_label)
        image_row.addStretch()
        image_row.setContentsMargins(30, 0, 30, 10)  # fine-tune spacing

        # Add centered image row to the bottom
        left_panel.addLayout(image_row)

        # Wrap in a QWidget and add to main layout
        left_container = QWidget()
        left_container.setLayout(left_panel)
        main_layout.addWidget(left_container, 3)

        # ─── MIDDLE: BUTTONS ───
        button_panel = QWidget()
        button_layout = QVBoxLayout(button_panel)
        button_layout.setSpacing(10)

        self.entities = []
        self.buttons = []
        for i in range(15):  # Create 10 buttons
            btn = QPushButton("Button")
            btn.setMinimumHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #114634;
                    color: white;
                    font-size: 14px;
                    border: 1px solid #555;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #444;
                }
                QPushButton:pressed {
                    background-color: #555;
                }
            """)
            btn.clicked.connect(lambda _, idx=i: self.lookup_entity_by_index(idx))
            button_layout.addWidget(btn)
            self.buttons.append(btn)
        button_layout.addStretch()
        main_layout.addWidget(button_panel, 2)

        # ─── RIGHT: INFO PANEL ───
        self.info_box = QTextEdit()
        self.info_box.setReadOnly(True)
        self.info_box.setFont(QFont("Arial", 16))
        self.info_box.setStyleSheet("""
            QTextEdit {
                background-color: #114634;
                color: #DDD;
                border: 1px solid #444;
            }
        """)
        main_layout.addWidget(self.info_box, 3)
    def lookup_entity_by_index(self, idx):
        if idx < len(self.entities):
            name = self.entities[idx]
            self.lookup_entity(name)
    def on_entity_info_loaded(self, name, result):
        self.response_cache[name] = (result, datetime.now())
        self.info_box.setText(result)
    def update_chart_from_data(self, entity_counts):
        # Sort top 10 entities by count
        sorted_entities = sorted(entity_counts.items(), key=lambda x: x[1], reverse=True)
        top_10 = sorted_entities[:10]
        top_names = [name for name, _ in top_10]

        # Step 2: Get remaining entities and pick 5 randomly
        remaining = [name for name, _ in sorted_entities[10:] if name not in top_names]
        filler_names = random.sample(remaining, min(5, len(remaining)))
        print(filler_names)
        # Step 3: Combine top + random fillers
        display_names = top_names + filler_names
        self.entities = display_names

        # Step 4: Show bar chart only for top 10
        chart = ""
        for name in display_names:
            count = entity_counts.get(name, 0)
            bar = "█" * math.ceil(count*0.5)
            chart += f"{name:<18} | {count:>2} {bar}\n"
        self.chart_label.setText(chart)

        # Step 5: Update buttons
        for i, btn in enumerate(self.buttons):
            if i < len(display_names):
                btn.setText(display_names[i])
                btn.setEnabled(True)
            else:
                btn.setText("Button")
                btn.setEnabled(False)

    def lookup_entity(self, name):
        if name in self.entities:
            if name in self.response_cache:
                cached_response, timestamp = self.response_cache[name]
                if datetime.now() - timestamp < self.cache_duration:
                    self.info_box.setText(f"{cached_response}\n\n🕒 (from cache)")
                    return
                else:
                    del self.response_cache[name]  # expired

            else:
                self.info_box.setText(f"🔍 Fetching info about {name}...")
                self.fetcher = InfoFetcher(name)
                self.fetcher.finished.connect(lambda result: self.on_entity_info_loaded(name, result))
                self.fetcher.start()

# ─── Kafka Consumer Setup ───
consumer = KafkaConsumer(
    'topic2',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: x.decode('utf-8')
)

latest_entity_counts = {}


def poll_kafka():
    try:
        msg_pack = consumer.poll(timeout_ms=100)
        for tp, messages in msg_pack.items():
            for msg in messages:
                raw_json = msg.value.replace("'", '"')
                data = json.loads(raw_json)
                top = sorted(data, key=data.get, reverse=True)
                latest_entity_counts.clear()
                for name in top:
                    latest_entity_counts[name] = data[name]
                window.update_chart_from_data(latest_entity_counts)
    except Exception as e:
        print("Kafka polling error:", e)


# ─── App Execution ───

app = QApplication(sys.argv)
window = MainWindow()
window.show()

# Poll Kafka every 2 minutes
timer = QTimer()
timer.timeout.connect(poll_kafka)
timer.start(15 * 1000)  # 2 minutes

# Do initial poll
poll_kafka()

sys.exit(app.exec_())
    
