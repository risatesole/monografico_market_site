
def views_tracer(func):
    def wrapper(request, *args, **kwargs):
        print(f"#################################################")
        print(f"Executing function: {func.__name__}")
        print(f"{request.POST.get("first_name")}")
        print(f"{request.POST.get("last_name")}")
        print(f"{request.POST.get("email")}")
        print(f"{request.POST.get("password")}")        
        response = func(request, *args, **kwargs)
        print(f"#################################################")
        return response
    return wrapper
