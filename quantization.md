## Quantization

Working with deep neural networks means dealing with lots and lots of numbers. These are the **parameters** — and there are billions of them.

They're numbers that get multiplied and added to other numbers in big matrix calculations on GPUs. They get set during training, and they're typically stored as **16-bit or 32-bit** numbers.

Most of you probably have a good sense of what that means: each number is made up of 16 or 32 binary digits — ones and zeros. So they can take a huge variety of values. They can be massive, and they have a lot of precision.

### The simplification

What if we stored these numbers at **lower precision**? Fewer bits per number?

Think of each weight like a **dimmer switch** for your lights. You turn the switch and the lights get brighter or darker.

- With **32 bits** (or even 16), there are so many possible settings that the knob turns *smoothly*. You can represent almost any number you can think of, with lots of decimal places.
- With **8 bits**, there are only **256** possible values.
- With **4 bits**, there are only **16** possible values.

Suddenly that dimmer switch isn't smooth anymore. It goes *click, click, click, click*. Your lights can't move continuously from bright to dark — they can only sit at 16 possible levels of brightness.

That's what it's like to take all of these parameters — all of these dimmer switches all over your neural network — and reduce the precision of every one of them.

Doing that is called **quantization**. You're *quantizing*: turning something smooth into something with discrete possible values, so you can squeeze more into less memory.

Go from a 16-bit floating point number down to a 4-bit number, and you've suddenly saved **four times the memory**. The calculations get way simpler too. That's why you do it.

But reducing the precision *does* degrade your neural network. It becomes less accurate. All the ways you measure how well it's doing go down.

**But they don't go down by much.** They go down by a little.

If you cut out three quarters of the weights, it would go down by **a lot**.

So it turns out that reducing precision is an efficient way to pack more information into less space. And we're not super sure *why* it works the way it does. We think it's because we didn't need so many parameters in the first place — so this just happens to be a good way to synthesize more of the data into a smaller space.

> **In short:** quantization reduces memory a lot, and only costs you a little accuracy. So we often do it. Very experimental, very hand-wavy — and it just kind of works.

---

## One more thing: NF4

For those of you who already know about bits and precision — when you hear "4-bit number" you're probably thinking of a **4-bit integer**. Literally the numbers 0 to 15.

And you're thinking: okay, but if these used to be proper floating point numbers and now they're numbers from 0 to 15, that's not going to work very well.

And the answer is: sure — but that's not what we do. It isn't a 4-bit integer.

We take those four bits and use them to **represent the floating point space** in some way. There's a technique for doing it, and the data type is called **NF4** — a 4-bit representation of floating point numbers, assuming they're normally distributed.

And again, it sort of works fine.
