 
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email(filedialog, simpledialog):
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpeg")])
    if file_path:
        recipient = simpledialog.askstring("Email", "Enter recipient email:")
        if recipient:
            try:
                msg = MIMEMultipart()
                msg['Subject'] = 'Your QR Code'
                msg['From'] = 'your_email@example.com'
                msg['To'] = recipient

                with open(file_path, 'rb') as f:
                    img = MIMEImage(f.read())
                    msg.attach(img)

                with smtplib.SMTP('smtp.example.com', 587) as server:
                    server.starttls()
                    server.login('your_email@example.com', 'your_password')
                    server.sendmail('your_email@example.com', recipient, msg.as_string())

                messagebox.showinfo("Success", "Email sent successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error sending email: {e}")
