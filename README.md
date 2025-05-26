# flet_gradient_text

It displays text with a colorful gradient and optional animation of the gradient.
#
## installation:
```bash
pip install flet_gradient_text
```
## 🔧 Parameters

- `text`(str): 	The text content to display
- `text_size`(int): optional	Font size of the text
- `text_weight`	ft.FontWeight, optional	Font weight (e.g., ft.FontWeight.BOLD)
- `text_style`(ft.TextStyle): optional	Custom text style (used alongside other text props)
- `animate`	(bool): default False	Enables shimmering animation
- `duration`(float or int): default 0.5,	Controls the speed of the animation (in seconds per loop)
- `gradient`: optional Custom gradient to apply over the text, default `LinearGradient`
- `on_click`(ft.ControlEvent) optional	Event handler when the text is clicked
- `on_hover`(ft.ControlEvent) optional	Event handler when hovering over the text

## 🧩 Usage

```python
import flet as ft
from flet_gradient_text import GradientText

def main(page: ft.Page):
    page.add(
        GradientText(
            text="Hello Gradient!",
            text_size=40,
            text_weight=ft.FontWeight.BOLD,
            animate=True,
            duration=1,
        )
    )

ft.app(target=main)
```


