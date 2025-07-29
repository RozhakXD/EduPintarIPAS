from flask import render_template, request, jsonify
from app.main import bp
from app.services.qna_service import QnAService

@bp.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'Maaf, kami tidak menemukan pertanyaan Anda. Mohon sertakan field "question" pada permintaan Anda.'}), 400

        question = data['question']
        if not question:
            return jsonify({'error': 'Tidak ada pertanyaan yang diberikan.'}), 400

        qna_service = QnAService()
        
        answer_text, confidence = qna_service.get_answer(question) 
        
        return jsonify({'answer': answer_text})

    except Exception as e:
        return jsonify({'error': 'Terjadi kesalahan internal pada server.'}), 500

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/chat')
def chat():
    return render_template('chat.html')