from .Schema import ReturnValueSchema
class ReturnValue:
    def success(self, value) -> ReturnValueSchema:
        ReturnValueSchema.is_success =  True
        ReturnValueSchema.value = value
        ReturnValueSchema.message = None
        return  ReturnValueSchema
    def failure(self, message) -> ReturnValueSchema:
        ReturnValueSchema.is_success =  True
        ReturnValueSchema.value = None
        ReturnValueSchema.message = message
        return  ReturnValueSchema    
