# dj-BateauThibo
start project
use command : 
'cd TME_webAPI_DJVAWS/mySearchEngine/'  
'py manage.py runserver'

initialise table : 
--> voir dans myRevendeurApp\management\refreshInfoProduct.py
use command : 
'cd TME_webAPI_DJVAWS/mySearchEngine/'
'py manage.py refreshInfoProduct'

# Exo 1: #
 ⎋ .../infoproduct/<int:id>/ −→ retourne les informations décrivant le produit d’identifiant id, avec les 10 champs originaux plus 1 champs supplémentaire.
 
![Capture](https://user-images.githubusercontent.com/43207346/110635992-04cf8900-81ac-11eb-99d7-6742757bcfe1.PNG)

 ⎋ .../infoproducts/ −→ retourne une liste des informations décrivant l’ensemble de tous les produits dans la base de donnée.
 
 ![Capture2](https://user-images.githubusercontent.com/43207346/110636444-8b846600-81ac-11eb-9efa-e63486a52af4.PNG)
 
# Exo 2: #
 ⎋ .../putonsale/<int:id>/<float:newprice>/ −→ dans les champs d’information correspondant au
produit id, affecter le champs sale à TRUE, en même temps, affecter le champs discount avec la valeur
newprice.

![Capture3](https://user-images.githubusercontent.com/43207346/110636889-16656080-81ad-11eb-821d-e86f14d69881.PNG)

 ⎋ .../removesale/<int:id>/ −→ dans les champs d’information correspondant au produit id, affecter le
champs sale à FALSE.

![Capture4](https://user-images.githubusercontent.com/43207346/110637188-6ba17200-81ad-11eb-8fdb-05abeda8eaf5.PNG)

 # Exo 3: #
 ⎋ .../incrementStock/<int:id>/<int:number>/ −→ dans les champs d’informations correspondant au
produit id, incrémente la valeur du champs quantityInStock par number unités, puis, retourner les
informations de ce produit après la mise à jour.

![Capture5](https://user-images.githubusercontent.com/43207346/110637490-ba4f0c00-81ad-11eb-9126-c8b895a8726f.PNG)

 ⎋ .../decrementStock/<int:id>/<int:number>/ −→ la même chose, en décrémentant au lieu d’incrémenter.
 
 ![Capture6](https://user-images.githubusercontent.com/43207346/110637663-ee2a3180-81ad-11eb-8969-dc88950f47cc.PNG)

# Exo 4: #
⎋ le champs sale de tout produit passe automatiquement à TRUE lorsque la valeur du champs quantityInStock
dépasse 16. Dans ce cas, le champs discount a pour valeur 80% la valeur du champs price si quantityInStock
est compris entre 16 et 64, discount a pour valeur 50% du price sinon.
le champs sale de tout produit passe automatiquement à FALSE lorsque la valeur du champs quantityInStock
ne dépasse pas 16.

--> voir dans myRevendeurApp\management\refreshPromotionProduct.py
use command : 
'cd TME_webAPI_DJVAWS/mySearchEngine/'
'py manage.py refreshPromotionProduct'

visuel de la table:
path: TME_webAPI_DJVAWS\mySearchEngine\db.sqlite3
![Capture7](https://user-images.githubusercontent.com/43207346/110638690-2716d600-81af-11eb-92ec-b9eb5f789164.PNG)
