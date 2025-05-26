import flet as ft
import asyncio


class GradientText(ft.ShaderMask):
    def __init__(
        self,
        text: str,
        text_size: int = None,
        text_weight: ft.FontWeight = None,
        text_style: ft.TextStyle = None,
        animate: bool = False,
        duration: float | int = 0.5,
        gradient: ft.LinearGradient | ft.RadialGradient | ft.SweepGradient = None,
        on_click: ft.ControlEvent = None,
        on_hover: ft.ControlEvent = None,
    ):

        self.text_size = text_size
        self.text_weight = text_weight
        self.text_style = text_style

        self.animation_pos = 0.0
        self.animate = animate
        self.duration = duration

        # default gradient
        self.gradient = (
            gradient
            if gradient
            else ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[
                    ft.Colors.RED_200,
                    ft.Colors.YELLOW_200,
                    ft.Colors.GREEN_200,
                    ft.Colors.BLUE_200,
                    ft.Colors.PURPLE_200,
                ],
                stops=[0.0, 0.2, 0.4, 0.6, 0.8],
            )
        )

        self.text = text

        # Animated gradient text Events
        self.on_click = on_click
        self.onhover = on_hover

        # ShaderMask initialization
        super().__init__(
            shader=self.gradient,
            blend_mode=ft.BlendMode.SRC_IN,
            content=ft.Container(
                ft.Text(
                    value=self.text,
                    size=self.text_size if self.text_size else 20,
                    weight=(
                        self.text_weight if self.text_weight else ft.FontWeight.W_100
                    ),
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextStyle(
                        letter_spacing=-1.5,
                        height=1,
                    ),
                ),
                margin=ft.margin.only(top=-5, bottom=self.text_size // 5),
                alignment=ft.alignment.center,
                on_click=self.on_click,
                on_hover=self.onhover,
            ),
        )

    def did_mount(self):
        if self.animate:
            self.page.run_task(self.animation_loop)

    async def animation_loop(self):
        while True:
            self.animation_pos += self.duration / 60
            if self.animation_pos > max(self.shader.stops):
                self.animation_pos = -0.0
            spread = 0.4 / (len(self.gradient.stops) - 1)
            self.shader.stops = [
                max(
                    0.0,
                    min(
                        1.0,
                        self.animation_pos
                        + (i - (len(self.gradient.stops) - 1) / 2) * spread,
                    ),
                )
                for i in range(len(self.gradient.stops))
            ]
            self.update()
            await asyncio.sleep(0.02)
