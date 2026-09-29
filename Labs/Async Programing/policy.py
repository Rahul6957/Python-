import asyncio


async def download_policy():
    print("Downloading")
    await asyncio.sleep(3)
    print ("Download")


    async def send_Mail():
        print("sending mail")

        await asyncio.sleep(4)
        print("Email sent")


async def main():
    await asyncio.gather(
        download_policy(),send_Mail()
    )

asyncio.run(main())


asyncio.run(main())

