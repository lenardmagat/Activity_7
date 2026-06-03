from Schema import ReturnValueSchema
class ReturnValue:
    def success(self, value) -> ReturnValueSchema:
        return  ReturnValueSchema(is_success = False, value = value, message = None)
    def failure(self, message) -> ReturnValueSchema:
        return  ReturnValueSchema(is_success = False, value = None, message = message)    
