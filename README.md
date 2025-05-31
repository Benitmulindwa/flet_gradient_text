# flet_gradient_text

It displays text with a colorful gradient and optional animation of the gradient.
#
## installation:
```bash
pip install flet_gradient_text
```
## 🔧 Parameters

- `text`(str): 	The text content to display
- `text_size`(optional): default `text_size=20`, Font size of the text
- `text_weight`: optional,	Font weight (e.g., ft.FontWeight.BOLD)
- `text_style`(optional): property of type `ft.TextStyle`
- `animate`	(bool): default `animate=False`, `True` to Enable animation
- `duration`(float or int): default `duration=0.5`, Controls the speed of the animation
- `gradient`: (optional) Custom gradient to apply over the text, default `LinearGradient`
- `on_click`(optional):	Event handler when the text is clicked
- `on_hover`(optional):	Event handler when hovering over the text

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


