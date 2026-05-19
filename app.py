from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
from flask import send_from_directory

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('templates/images', filename)

# Route for your main index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route for your detailed contact.html page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # This function now ONLY handles submissions from contact.html
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Saves the data to your original messages.txt file
        with open('messages.txt', 'a') as f:
            f.write(f"--- Contact Page Inquiry ---\n")
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Subject: {subject}\n")
            f.write(f"Message: {message}\n")
            f.write("-" * 20 + "\n")

        return render_template('contact.html', success=True)
    
    return render_template('contact.html', success=False)

# NEW route just for the homepage's contact form
@app.route('/inquiry', methods=['POST'])
def inquiry():
    # This function ONLY handles submissions from index.html
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        wishlist = request.form.get('wishlist')

        # Saves the data to the NEW inquiries.txt file
        with open('inquiries.txt', 'a') as f:
            f.write(f"--- Homepage Inquiry ---\n")
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            if wishlist:
                f.write(f"Wishlist Items: {wishlist}\n")
            f.write(f"Message: {message}\n")
            f.write("-" * 20 + "\n")
        
        # Redirects the user back to the homepage after submission
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

