import main
# main.main_run() အစား အောက်ကလို စမ်းကြည့်ပါ
if hasattr(main, 'main_run'):
    main.main_run()
elif hasattr(main, 'login'):
    main.login()
elif hasattr(main, 'menu'):
    main.menu()
else:
    print("Function name not found in main.so")
