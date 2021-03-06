﻿init:

#########################################################    
#Ресы для кошочки
#bg:
    #ext's
    image bg ext_dining_hall_away_night_uvao1_7dl = get_image_uvao_7dl("bg/ext_dining_hall_away_night_uvao1_7dl.jpg")
    image bg ext_dining_hall_away_night_uvao2_7dl = get_image_uvao_7dl("bg/ext_dining_hall_away_night_uvao2_7dl.jpg")
    image bg ext_washstand_sunset_7dl = get_image_uvao_7dl("bg/ext_washstand_sunset_7dl.jpg")
    
    #int's
    image bg int_mines_halt_spotlight_7dl = get_image_uvao_7dl("bg/int_mines_halt_spotlight_7dl.jpg")
    image bg int_catacombs_entrance_light_7dl = get_image_uvao_7dl("bg/int_catacombs_entrance_light_7dl.jpg")
    image bg int_sleep_hentai_office_7dl = get_image_uvao_7dl("bg/int_sleep_hentai_office_7dl.jpg")
    image bg int_sleep_hentai_office2_7dl = get_image_uvao_7dl("bg/int_sleep_hentai_office2_7dl.jpg")
    #Анимка спичек
    image match_lights: 
        contains: 
            'scenario_alt/DLC/UVAO/Pics/matches_tone.png' # оранжевенькая тонировка путь 1
            additive 1.0
        contains: 
            'scenario_alt/DLC/UVAO/Pics/matches_lightmask.png' # путь2
            xalign 0.5 yalign 1.0 
            function random_zoom # дрожание огонька
            repeat
    # Анимка бесконечных спичек
    image bg int_mine_crossroad_matches: 
        "bg black" with fade2
        0.5
        block:
            block:
                contains: 
                    'bg int_mine_crossroad' with fade2 
                contains: 
                    'scenario_alt/DLC/UVAO/Pics/matches_tone.png' #путь3
                    additive 1.0
                contains: 
                    'scenario_alt/DLC/UVAO/Pics/matches_lightmask.png' #путь4
                    xalign 0.5 yalign 1.0 
                    function random_zoom
                    repeat            
            4.0
            "bg black" with fade2
            4.0
            repeat
                   
#cg
    image cg d4_uv_pioner_lib_hiding_7dl = get_image_uvao_7dl("cg/d4_uv_pioner_lib_hiding_7dl.jpg")
    image cg d5_uv_photo_city_7dl = get_image_uvao_7dl("cg/d5_uv_photo_city_7dl.jpg")
    image cg d5_uv_photo_galaxy_7dl = get_image_uvao_7dl("cg/d5_uv_photo_galaxy_7dl.jpg")
    image cg d4_uv_bunker_hentai_7dl = get_image_uvao_7dl("cg/d4_uv_bunker_hentai_7dl.jpg")
    # Кошочка авторства Орики
    image uv_new_hentai1 = "images/1080/cg/epilogue_uv_hentai_1.jpg"
    image uv_new_hentai2 = "images/1080/cg/epilogue_uv_hentai_2.jpg"

    
#sounds
    $ phone_vibro = get_sfx_uvao_7dl("vibration-smartphone.ogg")
    $ match_lights = get_sfx_uvao_7dl("lighting-a-match.ogg")
    $ silence = get_sfx_uvao_7dl("silence_4sec.ogg")
    $ my_chrysalis_highwayman = get_music_uvao_7dl("my_chrysalis_highwayman.ogg")
    