import customtkinter as ctk
import modules.screen_app as m_app

width_input = 250
height_input = 50

font_size = ctk.CTkFont(
    family= "Arial",
    size= 20,
    weight= "bold"
)

text = ctk.StringVar()

text_input = ctk.CTkEntry(
    master= m_app.main_app.FRAME3,
    width= width_input,
    height= height_input,
    fg_color= "yellow",
    text_color= "black",
    font= font_size,
    textvariable= text
)

#text_input.place(x = m_app.main_app.APP_WIDTH // 2, y = m_app.main_app.APP_HEIGHT - height_input // 2, anchor = ctk.CENTER)
text_input.place(x = 260, y = m_app.main_app.APP_HEIGHT - height_input , anchor = ctk.CENTER)