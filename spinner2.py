# https://realpython.com/async-io-python/

from nicegui import ui
import asyncio
import time


def crazy3() -> None:
    print("crazy3")
    time.sleep(3)
    # await asyncio.sleep(2)
    print("cray3 ends")


async def crazy2() -> None:
    print("uhahahah")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("uhahahah2")


async def crazy() -> None:
    print("sleep")
    await asyncio.sleep(3)
    print("crazy starts here")
    crazy3()
    # await crazy2()
    # time.sleep(10)
    print("crazy finishes here")


async def slow_operation() -> None:
    with ui.spinner(size="lg") as spinner:
        print("in slow operation")
        # time.sleep(3)
        await crazy()
        # await crazy3()

        print("after sleep")
        spinner.set_visibility(False)


ui.button("Run spinner", on_click=slow_operation)

ui.run()
