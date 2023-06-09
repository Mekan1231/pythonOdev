# Python decorators
Decorator benºm anladığım kadarıyla c# dilindeki attuributelere benziyor. Pythonda herşey
nesne olarak görüldüği için bir fonksiyon başka bir fonksiyonu parametre olrak alabilir.
tabi bu özelliği decorator kullanmada kullanabiliriz
## Decorator kullanmadan
```python
def printer():
    print("hello world")

def display_info(func):
    def inner():
        print("Exacuting",func.__name__,"function")
        func()
        print("Finished exacution")
    return inner



result= display_info(printer)
result()
```

## Decorator kullanımı
```python
def display_info(func):
    def inner():
        print("Exacuting",func.__name__,"function")
        func()
        print("Finished exacution")
    return inner

@display_info
def printer():
    print("hello world")

printer()
```

# Pytest ile kullanılan decoratorlar
## pytest'te kullanılan decorator'ların tam listesi ve açıklamaları şunlardır:

__@pytest.fixture:__ Test işlevleri tarafından kullanılacak test verilerini veya hazırlık/kaynakları sağlayan bir fonksiyonu işaretlemek için kullanılır. Bu decorator, test fonksiyonunun argüman listesine eklenen bir parametrenin değerini döndürür.

__@pytest.mark.parametrize:__ Test fonksiyonlarının birden fazla kez çağrılmasını sağlamak için kullanılır. Bu decorator, test fonksiyonunun birden fazla kez çalıştırılmasına izin veren bir parametre listesi sağlar.

__@pytest.mark.skip:__ Bir test işlevinin geçici olarak atlanmasını sağlamak için kullanılır.

__@pytest.mark.xfail:__ Bir testin bilinen bir şekilde başarısız olacağını işaretlemek için kullanılır. Bu, testin hala çalışmasına ve çıktıda görünmesine neden olur, ancak başarısız olarak işaretlenir.

__@pytest.mark.skipif:__ Bir test işlevinin belirli bir koşulu karşılamadığı durumlarda atlanmasını sağlamak için kullanılır.

__@pytest.mark.timeout:__ Bir test işlevinin belirli bir sürede tamamlanması gerektiğini işaretlemek için kullanılır.

__@pytest.mark.order:__ Test işlevlerinin çalışma sırasını belirlemek için kullanılır.

__@pytest.mark.dependency:__ Testler arasında bağımlılık oluşturmak için kullanılır.

__@pytest.mark.usefixtures:__ Bir test fonksiyonunun önceden belirlenmiş bir hazırlık işlevi kullanmasını sağlamak için kullanılır.

# Test ekranı
![test ekranı](testpassed.png)