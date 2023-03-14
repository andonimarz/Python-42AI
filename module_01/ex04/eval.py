class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum(coef * len(word) for coef,word in zip(coefs,words))

    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        total = 0
        return sum(len(value) * coefs[index] for index, value in enumerate(words))

if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs,words))
    print(Evaluator.enumerate_evaluate(coefs,words))

    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs,words))
