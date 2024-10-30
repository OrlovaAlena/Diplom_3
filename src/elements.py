from selenium.webdriver.common.by import By


class Elements:
    # восстановление пароля
    RESTORE_PASSWORD_BUTTON = By.CSS_SELECTOR, "a[href = '/forgot-password'"
    RESTORE_PASSWORD_SIGN = By.XPATH, ".//h2[text()='Восстановление пароля']"

    RESTORE_BUTTON = By.XPATH, ".//form/button[text() = 'Восстановить']"
    CONFIRM_BUTTON = By.XPATH, ".//form/button[text() = 'Сохранить']"

    #  сброс пароля
    EYE_ICON = By.XPATH, ".//div[contains(@class,  'input__icon')]"
    PASSWORD_INPUT_ACT = By.XPATH, ".//div[contains(@class, 'input_status_active')]"

    # логин
    SIGN_IN_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    PASSWORD_INPUT = By.NAME, 'Пароль'
    CONFIRM_LOGIN_BUTTON = By.XPATH, ".//form/button[text() = 'Войти']"
    EMAIL_INPUT = By.XPATH, ".//div[label[text()='Email']]/input"

    # личный кабинет
    PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"
    ORDER_HISTORY = By.XPATH, ".//a[text()='История заказов']"
    EXIT = By.XPATH, ".//button[text()='Выход']"

    # header
    CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"
    ORDER_LIST = By.XPATH, ".//p[text()='Лента заказов']"

    # main
    # ingredient
    FLUORESCENT_BUN = By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/parent::a"
    COUNTER_FLOUR_BUN = (By.XPATH,
                         ".//p[contains(@class, 'counter_counter')]/../../p[text()='Флюоресцентная булка R2-D3']")

    ORDER = By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"

    # modal
    MODAL = By.XPATH, ".//h2[text() = 'Детали ингредиента']/../../.."
    MODAL_TITLE = By.XPATH, ".//h2[text() = 'Детали ингредиента']"
    MODAL_CLOSE_BUTTON = By.XPATH, ".//section[contains(@class, 'opened')]//button"
