
def chatbot_response(user_query):
    if "grease" in user_query.lower() or "factory floor" in user_query.lower():
        return ("You can use **PowerSolv HD** for heavy-duty degreasing. It's effective on concrete and steel surfaces. "
                "Use a 1:10 dilution for general cleaning, or 1:5 for heavy grease. Avoid using it on aluminum.")
    elif "aluminum" in user_query.lower() and "PowerSolv" in user_query:
        return ("**PowerSolv HD** is not recommended for aluminum. Consider another product.")
    elif "BioShine" in user_query or "sanitizer" in user_query.lower():
        return ("**BioShine Pro** is ideal for sanitizing food prep surfaces like stainless steel and plastic. "
                "Use a 1:128 dilution.")
    elif "scale" in user_query.lower() or "boiler" in user_query.lower():
        return ("**ScaleGuard X** is for mineral buildup. It’s ready-to-use on copper and stainless steel.")
    elif "vertical" in user_query.lower() or "foaming" in user_query.lower():
        return ("**FoamBlast 500** clings to vertical surfaces. Safe on tile, metal, plastic. Dilution 1:20.")
    elif "rust" in user_query.lower():
        return ("**RustXit Gel** removes rust from tools. Apply, wait 5–10 mins, and wipe clean.")
    else:
        return "Can you describe the surface and issue? I’ll try to recommend the best product."
