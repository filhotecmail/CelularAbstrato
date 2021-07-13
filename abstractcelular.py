from abc import abstractmethod


class AbstractCelular:

    @abstractmethod
    def Deps(callback):
        pass

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def chamadastelefonicas(acallnumber):
        pass

    @abstractmethod
    def textmessage(amessagetext):
        pass

 # region GetSetlter Name property

    def getname(self):
        return self.__name

    def setname(self, value):
        self.__name = value

    def delname(self):
        del self.__name

    def getrombios(self):
        return self.__name

    def setrombios(self, value):
        self.__name = value

    def delrombios(self):
        del self.__name

 # endregion

    name = property(getname, setname, delname, "Propriedade de Classe Nome")
    rombios = property(getrombios, setrombios, delrombios, "Propriedade de Classe Rom bios")