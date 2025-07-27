def create(tag, text,  **att):
    html = f"<{tag}"
    
    for key, value in att.items():
        html = html + f" {key}='{value}'"
        
    html = html + f">{text}</{tag}>"
    return html

tampil = create("p", "anjay mabar", id="paragraf")
print(tampil)

tampil = create("a", "ini link cok", href="www.google.com", style="shittt")
print(tampil)