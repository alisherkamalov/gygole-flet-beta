import flet as ft

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 625
    page.title = "Gygole"
    page.scroll = "auto"
    page.bgcolor = ft.colors.GREY_300
    
    
    
    page.window_resizable = False
    
    art = ft.Text(value="Статья", size=25)
    
    quiz = ft.Text(value="Quiz", size=25)
    
    task = ft.Text(value="Task", size=25)
    
    
    def back_home(event):
        
        index_back = page.navigation_bar.selected_index
        
        page.clean()
        
        if index_back == 0:
            
            page.add(start)
        
            page.add(ft.Row(
                [
                label1
        
                ]
                )
                )
            
            
    
            page.add(ft.Row(
                [
                    line_cont,
                cont_article1,
                
                ],
                )
                )
            
            page.add(ft.Row(
                [
                    line_cont,
                cont_article2,
                
                ],
                )
                )
            
            
            
            
        
        elif index_back == 1:
            
            
            
            page.add(start)
            
            page.add(ft.Row(
            [
            label_quizes
        
            ]
            )
            )
    
            page.add(ft.Row(
            [
                line_cont,
            cont_quizes1,
                
            ]
            )
            )
            
            page.add(ft.Row(
            [
                line_cont,
            cont_quizes2,
                
            ]
            )
            )
            
        elif index_back == 2:
            
            page.add(start)
            
            page.add(ft.Row(
            [
            my_task     
            ]
            )
            )
    
            page.add(ft.Row(
            [
            line_cont,
            cont_task1   
            ]
            )
            )
            
            page.add(ft.Row(
            [
            line_cont,
            cont_task2   
            ]
            )
            )
            
            
        
        page.update()
    
   
    back_to_home = ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_NEW, on_click=back_home)
    
    
    def find(event):
        
        def find_image(event):
            
            while True:
            
                image = entry_find.value
                
                
                if image == "":
                    error = ft.Text(value="Введите действующую ссылку")
                    page.add(ft.Row([error]))
                    page.update()
                    
                    break
                
                else:
                    
                    image_succes = ft.Container (
                        ft.Image(src=image),
                        height=150,
                        width=260,
                        border_radius=15,  
                                
                    )
                    cont_image = ft.Container (
                        bgcolor=ft.colors.BLUE_50,
                        width=265,
                        height=150,
                        border_radius=15,
                        padding=5,
                        content=ft.Stack([image_succes])
                        
                        
                    )
                    page.add(ft.Row([line_cont, cont_image]))
                    
                    page.update()
                    
                    break
                
                
            
                
        
        page.clean()
        
        page.add(start)
        
        entry_find = ft.TextField(label="Введите ссылку на гиф/картинку", width=250)
        
        
        
        btn_find = ft.FloatingActionButton(text="Найти", on_click=find_image, width=100, bgcolor=ft.colors.ON_PRIMARY)

        
        
        
            
        
        page.add(ft.Row(
            [
            entry_find,
            btn_find,
            
            ],
            
            
            )
            )
        
    
        
    def settings(event):
        
        
        
        
            
        def url(event):
            
            page.launch_url("https:/github.com/alisherkamalov/")
            
            page.update()
        
        page.clean()
        
        page.add(start)
        
        
        
        github_cont = ft.Container (
            
            bgcolor=ft.colors.SECONDARY,
            width=150,
            height=150,
            border_radius=15,
            margin=15,
            padding=15,
            content=ft.Text(value="My GitHub", bgcolor=ft.colors.SECONDARY, color="white", size=30),
            on_click=url,
            
            
        )
        
        
            
            
        
        
        
        page.add(ft.Row([github_cont]))
        
        
        
        
        
            
            
            
            
    
    
        
    btn_settings = ft.IconButton(icon=ft.icons.SETTINGS, on_click=settings)
    
    btn_find = ft.IconButton(icon=ft.icons.FIND_IN_PAGE, on_click=find)
    
    label1 = ft.Text(value="Статьи", size=25)
    
    label_quizes = ft.Text(value="Quizes", size=25)
    
    my_task = ft.Text(value="Мои Tasks", size=25)
    
    
    
    
    
    
    def navigate(event):
        
    
        
        index = page.navigation_bar.selected_index
        
        page.clean()
        
                
        if index == 0:
            
            
            page.add(start)
            
            
            page.add(ft.Row(
                [
                label1
        
                ]
                )
                )
            
            
    
            page.add(ft.Row(
                [
                    line_cont,
                cont_article1,
                
                ],
                )
                )
            
            page.add(ft.Row(
                [
                    line_cont,
                cont_article2,
                
                ],
                )
                )
            
            
            
            
        
        elif index == 1:
            
            page.add(start)
            
            page.add(ft.Row(
            [
            label_quizes
        
            ]
            )
            )
    
            page.add(ft.Row(
            [
                line_cont,
            cont_quizes1,
                
            ]
            )
            )
            
            page.add(ft.Row(
            [
                line_cont,
            cont_quizes2,
                
            ]
            )
            )
            
        elif index == 2:
            
            page.add(start)
            
            page.add(ft.Row(
            [
            my_task     
            ]
            )
            )
    
            page.add(ft.Row(
            [
            line_cont,
            cont_task1   
            ]
            )
            )
            
            page.add(ft.Row(
            [
            line_cont,
            cont_task2   
            ]
            )
            )
            
        elif index == 3:
            
            page.add(start)
            
            page.add(profile_cont)
            
            
            
            
            
            
        
        
    
    
        
        
    
    
    
    page.navigation_bar = ft.NavigationBar(
        destinations= [
            
            ft.NavigationDestination(icon=ft.icons.ARTICLE,label="Статьи"),
            ft.NavigationDestination(icon=ft.icons.QUIZ,label="Quiz"),
            ft.NavigationDestination(icon=ft.icons.TASK, label="Task"),
            ft.NavigationDestination(icon=ft.icons.ARTICLE,label="Профиль"),
            
        ],
        on_change=navigate,
        
        
    )
    def article1_info(event):
        
        page.clean()
        
        
        
        page.add(ft.Row([back_to_home, art]))
        
        info_article1 = ft.Text(value="Игорь линк текст текст текст текст текст текст", size=25, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87)
        
        info_article2 = ft.Text(value="Самый неподкупный, обьективный, авторитетный блогер. текст текст текст текст текст", size=20, color=ft.colors.BLACK87)
        
        
        
        cont_info_art_photo = ft.Container (
            ft.Image(src="https://media.tenor.com/7KLxeXFKfrgAAAAC/%D0%B8%D0%B3%D0%BE%D1%80%D1%8C%D0%BB%D0%B8%D0%BD%D0%BA-%D0%B8%D0%B3%D0%BE%D1%80%D1%8C.gif"),
            width=380,
            height=200,
            
            
            
            border_radius=15,
        )
        
        cont_photo_art = ft.Container (
            
            width=380,
            height=220,
            bgcolor=ft.colors.WHITE,
            padding=10,
            content=ft.Column([cont_info_art_photo]),
            
            
            border_radius=15,
        )
        
        cont_info_art_acc = ft.Container (
            
            width=125,
            height=50,
            bgcolor=ft.colors.WHITE,
            padding=15,
            content=ft.Row([ft.Icon(name=ft.icons.ACCOUNT_BOX, color=ft.colors.BLACK), ft.Text(value="@Admin", size=15)]),
            
            
            border_radius=10,
        )
        
        cont_art_title = ft.Container (
            width=380,
            height=100,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_article1])
        )
        
        cont_art_info = ft.Container (
            width=380,
            height=150,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_article2])
        )
        
        page.add(ft.Column([cont_photo_art, cont_info_art_acc, cont_art_title, cont_art_info]))
        
        
        
        
        
    def article2_info(event):
        
        page.clean()
        
        
        
        page.add(ft.Row([back_to_home, art]))
        
       
        
        info_article3 = ft.Text(value="Игорь Линк", size=25, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87)
        
        info_article4 = ft.Text(value="текст", color=ft.colors.BLACK87, size=20)
        
        cont_info_art_photo2 = ft.Container (
            ft.Image(src="https://virtus-img.cdnvideo.ru/images/og-jpg/plain/91/91b75ffee756182bc29e52b6895251b9.jpg"),
            width=380,
            height=200,
            
            
            
            border_radius=20,
        )
        
        cont_photo_art2 = ft.Container (
            
            width=380,
            height=220,
            bgcolor=ft.colors.WHITE,
            padding=10,
            content=ft.Column([cont_info_art_photo2]),
            
            
            border_radius=15,
        )
        
        cont_info_art_acc2 = ft.Container (
            
            width=125,
            height=50,
            bgcolor=ft.colors.WHITE,
            padding=15,
            content=ft.Row([ft.Icon(name=ft.icons.ACCOUNT_BOX, color=ft.colors.BLACK), ft.Text(value="@Admin", size=15)]),
            
            
            border_radius=10,
        )
        
        cont_art_title2 = ft.Container (
            width=380,
            height=100,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_article3])
        )
        
        cont_art_info2 = ft.Container (
            width=380,
            height=150,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_article4])
        )
        
        page.add(ft.Column([cont_photo_art2, cont_info_art_acc2, cont_art_title2, cont_art_info2]))
        
        
        
    def quizes1_info(event):
        
        page.clean()
        
        page.add(ft.Row([back_to_home, quiz]))
        
       
        
        info_quizes1 = ft.Text(value="Игорь линк", size=25, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87)
        
        info_quizes2 = ft.Text(value="текст", color=ft.colors.BLACK87, size=20)
        
        cont_info_photo_quiz = ft.Container (
            ft.Image(src="https://sun9-10.userapi.com/impf/c851436/v851436004/1d3368/Q0Z5toPHA80.jpg?size=1280x720&quality=96&sign=3da98f6bd22e008676ec6840965dbb82&c_uniq_tag=CCBJ6ChKG6wUDZC4iLxhQ5uYKTKgtrk1XNHDfuG5sbw&type=album"),
            width=380,
            height=200,
            
            
            
            border_radius=20,
        )
        
        cont_photo_quiz = ft.Container (
            
            width=380,
            height=220,
            bgcolor=ft.colors.WHITE,
            padding=10,
            content=ft.Column([cont_info_photo_quiz]),
            
            
            border_radius=15,
        )
        
        cont_info_quiz_acc = ft.Container (
            
            width=125,
            height=50,
            bgcolor=ft.colors.WHITE,
            padding=15,
            content=ft.Row([ft.Icon(name=ft.icons.ACCOUNT_BOX, color=ft.colors.BLACK), ft.Text(value="@Admin", size=15)]),
            
            
            border_radius=10,
        )
        
        cont_quiz_title = ft.Container (
            width=380,
            height=100,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_quizes1])
        )
        
        cont_quiz_info = ft.Container (
            width=380,
            height=150,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_quizes2])
        )
        
        page.add(ft.Column([cont_photo_quiz, cont_info_quiz_acc, cont_quiz_title, cont_quiz_info]))
    
        
    def quizes2_info(event):
        
        page.clean()
        
        page.add(ft.Row([back_to_home, quiz]))
        
        
        
        info_quizes3 = ft.Text(value="DeadP47", size=25, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87)
        
        info_quizes4 = ft.Text(value="текст", color=ft.colors.BLACK87, size=20)
        
        cont_info_photo_quiz2 = ft.Container (
            ft.Image(src="https://www.meme-arsenal.com/memes/1d36541945336f1350e68204a67edb75.jpg"),
            width=380,
            height=200,
            
            
            
            border_radius=20,
        )
        
        cont_photo_quiz2 = ft.Container (
            
            width=380,
            height=220,
            bgcolor=ft.colors.WHITE,
            padding=10,
            content=ft.Column([cont_info_photo_quiz2]),
            
            
            border_radius=15,
        )
        
        cont_info_quiz_acc2 = ft.Container (
            
            width=125,
            height=50,
            bgcolor=ft.colors.WHITE,
            padding=15,
            content=ft.Row([ft.Icon(name=ft.icons.ACCOUNT_BOX, color=ft.colors.BLACK), ft.Text(value="@Admin", size=15)]),
            
            
            border_radius=10,
        )
        
        cont_quiz_title2 = ft.Container (
            width=380,
            height=100,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_quizes3])
        )
        
        cont_quiz_info2 = ft.Container (
            width=380,
            height=150,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_quizes4])
        )
        
        page.add(ft.Column([cont_photo_quiz2, cont_info_quiz_acc2, cont_quiz_title2, cont_quiz_info2]))
        
    def my_task1_info(event):
        
        page.clean()
        
        page.add(ft.Row([back_to_home, task]))
        
        
        
        info_task1 = ft.Text(value="Игорь линк", size=25, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87)
        
        info_task2 = ft.Text(value="Выборы 2024", color=ft.colors.BLACK87, size=20)
        
        cont_info_photo_task = ft.Container (
            ft.Image(src="https://sun9-2.userapi.com/impf/c850628/v850628059/17c341/fJ5Y1UNWJE0.jpg?size=807x424&quality=96&sign=30e83a68bb75ff4a7befda5bb6d2db9e&c_uniq_tag=0VPP5IlyzvqSZoJEPardf-L-g0gJvJaj0o7ZarQppgo&type=album"),
            width=380,
            height=200,
            
            
            
            border_radius=20,
        )
        
        cont_photo_task = ft.Container (
            
            width=380,
            height=220,
            bgcolor=ft.colors.WHITE,
            padding=10,
            content=ft.Column([cont_info_photo_task]),
            
            
            border_radius=15,
        )
        
        cont_info_task_acc = ft.Container (
            
            width=125,
            height=50,
            bgcolor=ft.colors.WHITE,
            padding=15,
            content=ft.Row([ft.Icon(name=ft.icons.ACCOUNT_BOX, color=ft.colors.BLACK), ft.Text(value="@Admin", size=15)]),
            
            
            border_radius=10,
        )
        
        cont_task_title = ft.Container (
            width=380,
            height=100,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_task1])
        )
        
        cont_task_info = ft.Container (
            width=380,
            height=150,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_task2])
        )
        
        page.add(ft.Column([cont_photo_task, cont_info_task_acc, cont_task_title, cont_task_info]))
        
    def my_task2_info(event):
        
        page.clean()
        
        page.add(ft.Row([back_to_home, task]))
        
        
        
        info_task3 = ft.Text(value="DeadP47", size=25, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87)
        
        info_task4 = ft.Text(value="офигевает", color=ft.colors.BLACK87, size=20)
        
        
        cont_info_photo_task2 = ft.Container (
            ft.Image(src="https://media1.tenor.com/m/j2Hhy0_OTXYAAAAd/deadp47.gif"),
            width=380,
            height=200,
            
            
            
            border_radius=20,
        )
        
        cont_photo_task2 = ft.Container (
            
            width=380,
            height=220,
            bgcolor=ft.colors.WHITE,
            padding=10,
            content=ft.Column([cont_info_photo_task2]),
            
            
            border_radius=15,
        )
        
        cont_info_task_acc2 = ft.Container (
            
            width=125,
            height=50,
            bgcolor=ft.colors.WHITE,
            padding=15,
            content=ft.Row([ft.Icon(name=ft.icons.ACCOUNT_BOX, color=ft.colors.BLACK), ft.Text(value="@Admin", size=15)]),
            
            
            border_radius=10,
        )
        
        cont_task_title2 = ft.Container (
            width=380,
            height=100,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_task3])
        )
        
        cont_task_info2 = ft.Container (
            width=380,
            height=150,
            padding=10,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            content=ft.Stack([info_task4])
        )
        
        page.add(ft.Column([cont_photo_task2, cont_info_task_acc2, cont_task_title2, cont_task_info2]))
        
    
        
    
        
        page.update()
        
        
    line_cont = ft.Container (
        width=5,
        height=170,
        border_radius=15,
        bgcolor=ft.colors.GREEN_200
    )
        
    
    
    
    article1 = ft.Container (
        
        ft.Image (src="https://media.tenor.com/7KLxeXFKfrgAAAAC/%D0%B8%D0%B3%D0%BE%D1%80%D1%8C%D0%BB%D0%B8%D0%BD%D0%BA-%D0%B8%D0%B3%D0%BE%D1%80%D1%8C.gif"),
        
        height=150,
        width=400,
        border_radius=15,
        
        
        on_click=article1_info,
        
    )
        
        
    cont_article1 = ft.Container (
        width=260,
        height=160,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        padding=5,
        content=ft.Column ([article1])
        
        
        
        
        
        
        
    )
    
    article2 = ft.Container (
        ft.Image (src="https://virtus-img.cdnvideo.ru/images/og-jpg/plain/91/91b75ffee756182bc29e52b6895251b9.jpg"),
        height=350,
        width=350,
        border_radius=20,
        on_click=article2_info
        
        
    )
    
    cont_article2 = ft.Container (
        width=260,
        height=160,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        padding=5,
        content=ft.Stack([article2])
        
    )
    
    
    
    
    
    quizes1 = ft.Container (
        ft.Image (src="https://sun9-10.userapi.com/impf/c851436/v851436004/1d3368/Q0Z5toPHA80.jpg?size=1280x720&quality=96&sign=3da98f6bd22e008676ec6840965dbb82&c_uniq_tag=CCBJ6ChKG6wUDZC4iLxhQ5uYKTKgtrk1XNHDfuG5sbw&type=album"),
        height=150,
        width=270,
        border_radius=15,
        on_click=quizes1_info,
        
        
    )
       
    cont_quizes1 = ft.Container (
        
        width=270,
        height=160,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        padding=5,
        content=ft.Column ([quizes1])
        
    ) 
        
    
        
    
    
    quizes2 = ft.Container (
        ft.Image (src="https://www.meme-arsenal.com/memes/1d36541945336f1350e68204a67edb75.jpg"),
        height=150,
        width=270,
        border_radius=15,
        on_click=quizes2_info
        
    )
    
    cont_quizes2 = ft.Container (
        
        width=270,
        height=160,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        padding=5,
        content=ft.Column ([quizes2])
        
    ) 
    
    my_task1 = ft.Container (
        ft.Image (src="https://sun9-2.userapi.com/impf/c850628/v850628059/17c341/fJ5Y1UNWJE0.jpg?size=807x424&quality=96&sign=30e83a68bb75ff4a7befda5bb6d2db9e&c_uniq_tag=0VPP5IlyzvqSZoJEPardf-L-g0gJvJaj0o7ZarQppgo&type=album"),
        height=150,
        width=275,
        border_radius=25,
        on_click=my_task1_info
        
    )
    
    cont_task1 = ft.Container (
        
        width=280,
        height=160,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        padding=5,
        content=ft.Column ([my_task1])
        
    ) 
    
    my_task2 = ft.Container (
        ft.Image (src="https://media1.tenor.com/m/j2Hhy0_OTXYAAAAd/deadp47.gif"),
        height=150,
        width=275,
        border_radius=15,
        on_click=my_task2_info
        
    )
    
    cont_task2 = ft.Container (
        
        width=280,
        height=160,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        padding=5,
        content=ft.Column ([my_task2])
        
    ) 
    
    logo = ft.Container(
        ft.Image(src="https://github.com/alisherkamalov/gygole_project/blob/main/logo5.png?raw=true"),
        height=50,
        width=250,
        bgcolor=ft.colors.WHITE,
        border_radius=15
        
    )
    cont_logo = ft.Container (
        width=250,
        height=50,
        padding=5,
        content=ft.Stack([logo])
    )
    
    profile_info = ft.Text(value="Информация о аккаунте:", size=25)
    
    profile_text = ft.Text(value="Имя: Admin\nLink: @Admin", size=20)
    
    
    
    profile_cont = ft.Container (
        width=350,
        height=150,
        bgcolor=ft.colors.WHITE,
        content=ft.Column([profile_info, profile_text]),
        padding=10,
        border_radius=10
    )
    
    
    start = ft.Row(
        [
        btn_settings,
        cont_logo,
        btn_find,
        
        ]
        )
    
    page.add(start)

    
    
    
    
    
    
    
    
    
    
    
    
    
    

    page.update()
    

ft.app(target=main)

