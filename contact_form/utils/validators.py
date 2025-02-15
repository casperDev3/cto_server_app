def form_validator(data):
    required_fields = ['name', 'email', 'message']

    for field in required_fields:
        if not data.get(field):
            return {
                "success": False,
                "message": f"Please enter a {field}",
                "status_code": 400,
            }

    return {"success": True}