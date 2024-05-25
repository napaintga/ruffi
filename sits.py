# напиши модуль для підрахунку кількості присідань

class Sits(Label):
    
    def __init__(self, total, **kwargs):
        pass

    def next(self, *args):
        # if keys[K_SPACE]:
        #     jumping = True
        #     hang_start_time = time.get_ticks()

        # if jumping:
        #     if jump_count < dino_jump_height:
        #         dino.rect.y -= dino_jump_speed
        #         jump_count += dino_jump_speed
        #     else:
        #         if time.get_ticks() - hang_start_time +1 >= hang_time:
        #             jumping = False
        #             jump_count = 0
        # else:
        #     if dino.rect.y < 335:
        #         dino.rect.y += dino_jump_speed
        if keys[K_SPACE] and jump_count == 0:
            jump_count = dino_jump_height

        if jump_count > 0:
            dino.rect.y -= dino_jump_speed
            jump_count -= dino_jump_speed
        else:
            if dino.rect.y < 335:
                dino.rect.y += dino_jump_speed
