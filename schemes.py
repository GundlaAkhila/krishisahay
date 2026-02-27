def get_scheme_info(name):
    schemes = {
        "pmkisan": "PM-KISAN gives ₹6000 per year to eligible farmers.",
        "fasalbima": "Crop insurance scheme for farmers.",
        "soilcard": "Provides soil health testing report."
    }
    
    key = name.lower()
    return {"info": schemes.get(key, "Scheme not found")}