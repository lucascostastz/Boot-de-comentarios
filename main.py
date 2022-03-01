from PyQt6 import uic, QtWidgets
import pyautogui
from selenium import webdriver
import time


def comecar():

    # Abrir navegador
    navegador = webdriver.Chrome("chromedriver")
    # Abrir link do instagram
    navegador.get("https://www.instagram.com/")

    # esperar 2 segundos
    time.sleep(2)

    # Digitar nome de usuário
    usuario = primeira_tela.lineEdit_2.text()
    navegador.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(usuario)

    # Esperar 1 segundos
    time.sleep(1)

    # Digitar senha
    senha = primeira_tela.lineEdit_3.text()
    navegador.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)

    # Esperar 1 segundo
    time.sleep(1)

    # Clicar no botão entrar
    navegador.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[3]/button/div').click()

    # Tempo
    time.sleep(3)

    # Clicar no botão agora não
    navegador.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

    # Tempo
    time.sleep(3)
    # Clicar no botão de desaivar notificações
    navegador.find_element_by_xpath(
        '/html/body/div[5]/div/div/div/div[3]/button[2]').click()

    # Tempo+
    time.sleep(3)

    pyautogui.press('F6')

    time.sleep(1)
    link = primeira_tela.Inserir_Link.text()

    pyautogui.write(link)
    time.sleep(1)
    pyautogui.press('Enter')


# Clicar em Comentar
    navegador.find_element_by_class_name("Ypffh").click()
    # Tempo
    time.sleep(1)

    # Comentar
    comentario = primeira_tela.lineEdit_5.text()
    navegador.find_element_by_class_name("Ypffh").send_keys(comentario)

    # Tempo
    time.sleep(1)
    pyautogui.press('Enter')


############################# TEMPO #############################

    def tempo():
        # Tempo Selecionado
        tempo = primeira_tela.comboBox.currentText()
        time.sleep(int(tempo)*(60))

        # Comentar
        comentario = primeira_tela.lineEdit_5.text()
        navegador.find_element_by_class_name("Ypffh").send_keys(comentario)
        pyautogui.press('Enter')
    tempo()
    while True:
        tempo()


def sair():
    primeira_tela.close()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("tela.ui")

primeira_tela.pushButton_2.clicked.connect(comecar)
primeira_tela.pushButton_3.clicked.connect(sair)
primeira_tela.comboBox.addItems(
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])


primeira_tela.show()
app.exec()
