import task2_chemistry_upd as t2
#одновременный запуск всех тестов может привести к неверным результатам
#лучше запускать тесты по одному (или с очень коротким перерывом)

class TestChemistry:
    def test_c0(self):
        with open("input.txt", "w") as f:
            f.write("C = 0")

        try:
            t2.molecula_count("C(2)H(6)")
            assert False
        except t2.UnknownElementError: # Водород не содержится в полученном наборе атомов 
            assert True
        except Exception:
            assert False

    def test_c2h2(self):
        with open("input.txt", "w") as f:
            f.write("C = 2, H = 2")
        
        t2.molecula_count("C(2)H(2)")

        with open("output.txt", "r") as f:
            assert int(f.read()) == 1

    def test_c2h6o(self):
        with open("input.txt", "w") as f:
            f.write("C = 12, H = 36, O = 6")
        
        t2.molecula_count("C(2)H(6)O(1)")

        with open("output.txt", "r") as f:
            assert int(f.read()) == 6

    def test_ch3cooh(self):
        with open("input.txt", "w") as f:
            f.write("C = 10, H = 12, O = 9")
        
        t2.molecula_count("C(1)H(3)O(1)O(1)H(1)")

        with open("output.txt", "r") as f:
            assert int(f.read()) == 3

    def test_c2h5oc2h5(self):
        with open("input.txt", "w") as f:
            f.write("C = 10, H = 20, O = 9")
        
        t2.molecula_count("C(1)C(1)H(1)H(1)H(1)H(1)H(1)O(1)C(2)H(5)")

        with open("output.txt", "r") as f:
            assert int(f.read()) == 2

    def test_unknown_elements(self):
        with open("input.txt", "w") as f:
            f.write("C = 4, H = 10, O = 20")

        try:
            t2.molecula_count("H(3)P(1)O(4)") # Фосфор - неизвестный элемент (нет в списке)
            assert False
        except t2.UnknownElementError:
            assert True
        except Exception:
            assert False

    def test_oxytocine(self):
        with open("input.txt", "w") as f:
            f.write("oxytocine")
        
        t2.molecula_count("C(43)H(66)N(12)O(12)S(2)") # формула окситоцина

        with open("output.txt", "r") as f:
            assert int(f.read()) == 1
    
    def test_double_insulin(self):
        with open("input.txt", "w") as f:
            f.write("insulin, insulin")
        
        t2.molecula_count("C(257)H(383)N(65)O(77)S(6)") # удвоенная формула инсулина

        with open("output.txt", "r") as f:
            assert int(f.read()) == 2

    def test_mixed_compounds(self):
        with open("input.txt", "w") as f:
            f.write("insulin, oxytocine, dopamine, serotonin")

        t2.molecula_count("C(4)H(10)")

        with open("output.txt", "r") as f:
            assert int(f.read()) == 47
    
    def test_mixed_input(self):
        with open("input.txt", "w") as f:
            f.write("insulin, C = 10, N = 40, Ca = 1, dopamine, P = 4")

        t2.molecula_count("C(4)H(10)")

        with open("output.txt", "r") as f:
            assert int(f.read()) == 39

    def test_wrong_input_container(self):
        with open("input.txt", "w") as f:
            f.write("C == 1, H == 4, O == 3") # недостимый формат ввода (==)

        try:
            t2.molecula_count("C(1)H(4)O(3)")
            assert False
        except t2.WrongInputError:
            assert True
        except Exception:
            assert False

    def test_wrong_input_molecula(self):
        with open("input.txt", "w") as f:
            f.write("C = 1, H = 4, O = 3")

        try:
            t2.molecula_count("c2h5oh") # неверный ввод молекулы
            assert False
        except t2.WrongInputError:
            assert True
        except Exception:
            assert False

    def test_unknown_compound(self):
        with open("input.txt", "w") as f:
            f.write("qwerty") # соединение с таким названием отсутствует в списке соединений (по крайней мере, сейчас)

        try:
            t2.molecula_count("C(1)H(4)O(1)")
            assert False
        except t2.UnknownElementError:
            assert True
        except Exception:
            assert False


    # дополнительный тест, фактически дублирующий тест test_wrong_input_molecula
    def test_sweetie_pie(self):
        with open("input.txt", "w") as f:
            f.write("Olya")
            
        try:
            # исключение будет брошено раньше, чем функция дойдёт до чтения молекулы от пользователя
            t2.molecula_count("I can write anything here, the program will crash sooner anyway, so:\
            \nLove is being stupid together.")
            assert False
        except t2.UnknownElementError:
            assert True
        except Exception:
            assert False