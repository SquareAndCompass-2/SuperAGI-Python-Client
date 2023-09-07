from superagi_client.lib.logger import logger


class InternalServerErrorException(Exception):
    def __init__(
        self, message="Internal Server Error", status_code=500, additional_info=None
    ):
        self.message = message
        self.status_code = status_code
        self.additional_info = additional_info
        super().__init__(
            f"{self.message} => {self.additional_info}"
            if self.additional_info
            else self.message
        )

        logger.error(
            f"BadRequestException: {self.message}, Status Code: {self.status_code}, "
            f"Additional Info: {self.additional_info}"
        )