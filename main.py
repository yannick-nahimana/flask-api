# from flask import Flask,jsonify,request
# from flask_cors import CORS
# import yagmail
import os
# from dotenv import find_dotenv,load_dotenv


# #app instance 
# app = Flask(__name__)
# CORS(app)

# dotenv_path = find_dotenv()

# load_dotenv(dotenv_path)
# sender = 'yannconnections@gmail.com'



# sender = 'yannconnections@gmail.com'
# receiver ='consultantyannick@gmail.com'
# yag = yagmail.SMTP(user = sender, password=os.getenv('google_code'))

# @app.route('/',methods=['GET'])
# def return_home():
#     return '<h1>API Welcome message</h1>'



# @app.route('/api/send-email', methods=['POST','GET'])
# def send_email():
#     data = request.get_json()
#     email = data.get('email')
#     message = data.get('message')
#     name= data.get('name')
#     subject = data.get('subject')

#     # Add your email sending logic here
    

#     content = f'''
#     From : {name}
#     Email : {email}
#     Message:
#     {message}
#     '''
#     yag.send(to=receiver,subject=subject,contents=content)
#     return jsonify({"message": "Email sent successfully"}), 200



# if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 8080))
    # app.run(debug=True, host='0.0.0.0', port=port)




from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Adjust origins as needed

@app.route('/api/your-endpoint', methods=['POST'])
def your_endpoint():
    data = request.get_json()
    # Process the data
    return jsonify({"message": "Data received", "data": data})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)













