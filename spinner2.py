# https://realpython.com/async-io-python/

from nicegui import ui
import asyncio
import time


async def crazy2() -> None:
    print("uhahahah")
    await asyncio.sleep(5)
    # time.sleep(5)


async def crazy() -> None:
    print("crazy starts here")
    await asyncio.sleep(3)
    await crazy2()
    # time.sleep(10)
    print("crazy finishes here")


async def slow_operation() -> None:
    with ui.spinner(size="lg") as spinner:
        print("in slow operation")
        await crazy()

        print("after sleep")
        print(spinner)
        spinner.set_visibility(False)


ui.button("Run spinner", on_click=slow_operation)

ui.run()
