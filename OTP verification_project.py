import math
import random
import smtplib

# Generate a 6-digit OTP
digits = "0123456789"
OTP = "".join([digits[math.floor(random.random() * 10)] for i in range(6)])
otp_message = OTP + " is your OTP"
print("Generated OTP:", OTP)  # This is for debugging; remove it in production

# Set up the SMTP server
try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail Account", "Your App Password")  # Use an app-specific password for better security
    
    # Get the recipient email address
    emailid = input("Enter your email: ")
    
    # Send the email
    s.sendmail("Your Gmail Account", emailid, otp_message)
    s.quit()
    
    # Prompt user to enter the received OTP
    a = input("Enter Your OTP >>: ")
    
    # Verify OTP
    if a == OTP:
        print("Verified")
    else:
        print("Please check your OTP again")
except Exception as e:
    print(f"Error: {e}")
