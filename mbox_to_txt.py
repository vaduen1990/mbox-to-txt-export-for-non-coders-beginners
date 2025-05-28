import mailbox

mbox = mailbox.mbox("casestudy.mbox")

with open("emails_output.txt", "w", encoding="utf-8") as out:
    for i, msg in enumerate(mbox, 1):
        subject = msg['subject'] or "No Subject"
        sender  = msg['from']    or "Unknown Sender"
        date    = msg['date']    or "No Date"

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type()=="text/plain":
                    charset = part.get_content_charset() or "utf-8"
                    body = part.get_payload(decode=True)\
                               .decode(charset, errors="replace")
                    break
        else:
            body = msg.get_payload(decode=True)\
                      .decode(msg.get_content_charset() or "utf-8", errors="replace")

        out.write(f"--- Email #{i} ---\n")
        out.write(f"From: {sender}\nDate: {date}\nSubject: {subject}\n\n")
        out.write(body + "\n\n" + "-"*40 + "\n\n")

print("Emails exported to emails_output.txt")
