import time
from nicegui import run, ui


def heavy_computation() -> str:
    time.sleep(5)

    return "Done!"


async def start_computation():
    result = await run.cpu_bound(heavy_computation)

    ui.notify(result)


async def slow_operation():
    print("in slow operation")

    spinner = ui.spinner(size="lg")

    await start_computation()

    spinner.set_visibility(False)


ui.button("Run spinner", on_click=slow_operation)

ui.run()
