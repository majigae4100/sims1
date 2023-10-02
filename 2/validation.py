from file2 import BuildError

class Validator:
    def Check(self, error: BuildError):
        if(isinstance(error, BuildError)):
            if(error.Limit < error.Amount):
                raise BuildError(error.Amount, error.Limit)
            return True
