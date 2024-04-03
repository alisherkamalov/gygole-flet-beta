import flet as ft

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 625
    page.title = "Gygole"
    page.scroll = "auto"
    
    
    
    page.window_resizable = False
    
   
    
    
    
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
                        height=100,
                        width=170,
                        border_radius=15,  
                                
                    )
                    page.add(ft.Row([image_succes]))
                    
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
        
        
        
        def theme(event):
            
            page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        
            page.update()
            
        def url(event):
            
            page.launch_url("https:/github.com/alisherkamalov/")
            
            page.update()
        
        page.clean()
        
        page.add(start)
        
        setting_cont = ft.Container (
            bgcolor=ft.colors.SECONDARY,
            width=150,
            height=150,
            border_radius=15,
            margin=15,
            padding=15,
            content=ft.Text(value="Theme mode", bgcolor=ft.colors.SECONDARY, color="white", size=30),
            on_click=theme,
            
            
                        
            
            )
        
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
        
        
            
            
        
        
        
        page.add(ft.Row([setting_cont, github_cont]))
        
        
        
        
        
            
            
            
            
    
    
        
    btn_settings = ft.IconButton(icon=ft.icons.SETTINGS, on_click=settings)
    
    btn_find = ft.IconButton(icon=ft.icons.FIND_IN_PAGE, on_click=find)
    
    label1 = ft.Text(value="Статьи")
    
    label_quizes = ft.Text(value="Quizes")
    
    my_task = ft.Text(value="Мои Tasks")
    
    
    
    
    
    
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
                article1,
                article2
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
            quizes1,
            quizes2        
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
            my_task1,
            my_task2    
            ]
            )
            )
            
            
            
            
        
        
    
    
        
        
    
    
    
    page.navigation_bar = ft.NavigationBar(
        destinations= [
            ft.NavigationDestination(icon=ft.icons.TASK, label="Task"),
            ft.NavigationDestination(icon=ft.icons.QUIZ,label="Quiz"),
            ft.NavigationDestination(icon=ft.icons.ARTICLE,label="Статьи")
        ],
        on_change=navigate
        
    )
    def article1_info(event):
        
        page.clean()
        
        page.add(start)
        
        page.add(article1)
        
        info_article1 = ft.Text(value="Игорь линк", size=25)
        
        info_article2 = ft.Text(value="Текст")
        
        page.add(ft.Column ([
            info_article1,
            info_article2
        ]))
        
    def article2_info(event):
        
        page.clean()
        
        page.add(start)
        
        page.add(article2)
        
        info_article3 = ft.Text(value="DeadP47", size=25)
        
        info_article4 = ft.Text(value="кушает чокопай")
        
        page.add(ft.Column ([
            info_article3,
            info_article4
        ]))
        
    def quizes1_info(event):
        
        page.clean()
        
        page.add(start)
        
        page.add(quizes1)
        
        info_quizes1 = ft.Text(value="Игорь линк", size=25)
        
        info_quizes2 = ft.Text(value="текст")
        
        page.add(ft.Column ([
            info_quizes1,
            info_quizes2
        ]))
        
    def quizes2_info(event):
        
        page.clean()
        
        page.add(start)
        
        page.add(quizes2)
        
        info_quizes3 = ft.Text(value="DeadP47", size=25)
        
        info_quizes4 = ft.Text(value="текст")
        
        page.add(ft.Column ([
            info_quizes3,
            info_quizes4
        ]))
        
    def my_task1_info(event):
        
        page.clean()
        
        page.add(start)
        
        page.add(my_task1)
        
        info_task1 = ft.Text(value="Игорь линк", size=25)
        
        info_task2 = ft.Text(value="Выборы 2024")
        
        page.add(ft.Column ([
            info_task1,
            info_task2
        ]))
        
    def my_task2_info(event):
        
        page.clean()
        
        page.add(start)
        
        page.add(my_task2)
        
        info_task3 = ft.Text(value="DeadP47", size=25)
        
        info_task4 = ft.Text(value="офигевает")
        
        page.add(ft.Column ([
            info_task3,
            info_task4
        ]))
    
        
    
        
    
        
        page.update()
        
    
    
    article1 = ft.Container (
        
        ft.Image (src="https://media.tenor.com/7KLxeXFKfrgAAAAC/%D0%B8%D0%B3%D0%BE%D1%80%D1%8C%D0%BB%D0%B8%D0%BD%D0%BA-%D0%B8%D0%B3%D0%BE%D1%80%D1%8C.gif"),
        
        height=100,
        width=170,
        border_radius=15,
        
        
        on_click=article1_info,
        
        
        
        
        
        
    )
    
    article2 = ft.Container (
        ft.Image (src="https://media1.tenor.com/m/U8r-wOsLLIYAAAAd/deadp47.gif"),
        height=100,
        width=150,
        border_radius=15,
        on_click=article2_info
        
        
    )
    
    quizes1 = ft.Container (
        ft.Image (src="https://sun9-10.userapi.com/impf/c851436/v851436004/1d3368/Q0Z5toPHA80.jpg?size=1280x720&quality=96&sign=3da98f6bd22e008676ec6840965dbb82&c_uniq_tag=CCBJ6ChKG6wUDZC4iLxhQ5uYKTKgtrk1XNHDfuG5sbw&type=album"),
        height=100,
        width=170,
        border_radius=15,
        on_click=quizes1_info
        
    )
    
    quizes2 = ft.Container (
        ft.Image (src="https://www.meme-arsenal.com/memes/1d36541945336f1350e68204a67edb75.jpg"),
        height=100,
        width=170,
        border_radius=15,
        on_click=quizes2_info
        
    )
    
    my_task1 = ft.Container (
        ft.Image (src="https://sun9-2.userapi.com/impf/c850628/v850628059/17c341/fJ5Y1UNWJE0.jpg?size=807x424&quality=96&sign=30e83a68bb75ff4a7befda5bb6d2db9e&c_uniq_tag=0VPP5IlyzvqSZoJEPardf-L-g0gJvJaj0o7ZarQppgo&type=album"),
        height=100,
        width=180,
        border_radius=15,
        on_click=my_task1_info
        
    )
    
    my_task2 = ft.Container (
        ft.Image (src="https://media1.tenor.com/m/j2Hhy0_OTXYAAAAd/deadp47.gif"),
        height=100,
        width=170,
        border_radius=15,
        on_click=my_task2_info
        
    )

    logo = ft.Container(
        ft.Image(src="https://github.com/alisherkamalov/gygole_project/blob/main/logo5.png?raw=true"),
        height=50,
        width=250,
        
    )
    
    start = ft.Row(
        [
        btn_settings,
        logo,
        btn_find,
        
        ]
        )
    
    page.add(start)

    
    
    
    
    
    
    
    
    
    
    
    
    
    

    page.update()

ft.app(target=main)
