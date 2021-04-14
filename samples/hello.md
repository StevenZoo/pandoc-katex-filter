---
title: "Sample Markdown"
---

Here is some inline text: $a+b$

Here is some text in display mode: $$a+b$$


It starts its own line, and is centered.


A matrix:

$$
\begin{bmatrix}
   a & b \\
   c & d
\end{bmatrix}
$$

##### Note
This expression does *not* work due to the space between the $ delimiter and the TeX expression: $ a+b $

Pandoc will see $ a+b $ as just text, and render accordingly. It won't be considered as a math expression.

