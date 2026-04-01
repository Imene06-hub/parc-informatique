import sqlite3
def connecter():
    conn =sqlite3.connect('projetihm.db')
    cur = conn.cursor()
#Si la table n'existe pas va la créer
    cur.execute("""CREATE TABLE IF NOT EXISTS equipements(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    marque TEXT NOT NULL,
    modele TEXT NOT NULL,
    num_serie TEXT UNIQUE NOT NULL,
    localisation TEXT NOT NULL,
    etat TEXT NOT NULL
    )
    """)
    conn.commit()
    return conn
#Ajouter un equipement 
def ajouter_equipement(type,marque,modele,num_serie,localisation,etat):
    conn = connecter()
    cur=conn.cursor()
    cur.execute("INSERT INTO equipements (type, marque, modele, num_serie, localisation, etat) VALUES (?,?,?,?,?,?)",(type,marque,modele,num_serie,localisation,etat))
    conn.commit()
    conn.close()
#Rechercher un equipement
def rechercher_equipement(critere,valeur):
    conn=connecter()
    cur=conn.cursor()
    #f permet d'inserer une variable dans une chaine de caractères
    cur.execute(f"SELECT * FROM equipements WHERE {critere} LIKE ?",('%' + valeur + '%',))
    res=cur.fetchall()
    conn.close()
    return res
def recherche_generique(valeur):
    conn=connecter()
    cur=conn.cursor()
    cur.execute("SELECT * FROM equipements WHERE type LIKE ? OR marque LIKE ? OR modele LIKE ?OR num_serie LIKE ? OR localisation LIKE ?",('%' +valeur+ '%','%' +valeur+ '%','%' +valeur+ '%','%' +valeur+ '%','%' +valeur+ '%'))
    res=cur.fetchall()
    conn.close()
    return res
#Modifier un equipement
def modifier_equipement(id_equi,nouv_type,nouv_marque,nouv_modele,nouv_num,nouv_localisation,nouv_etat):
    conn=connecter()

    cur=conn.cursor()
    cur.execute("""
                    UPDATE equipements
                    SET type = ?, marque = ?, modele = ?,num_serie= ?, localisation = ?, etat= ?
                    WHERE id = ?
                    """,(nouv_type,nouv_marque,nouv_modele,nouv_num,nouv_localisation,nouv_etat,id_equi))
    conn.commit()
    conn.close()
#Supprimer un equipement
def supprimer_equipement(num_serie):
    conn=connecter()
    cur=conn.cursor()
    cur.execute("DELETE FROM equipements WHERE num_serie= ?",(num_serie,))
    conn.commit()
    conn.close()
#Afficher tout le parc informatique
def trier(trie):
    conn=connecter()
    cur=conn.cursor()
    res= cur.execute(f"SELECT * FROM equipements ORDER BY {trie} ASC")
    res=cur.fetchall()
    conn.close()
    return res
def afficher_tous():
    conn=connecter()
    cur=conn.cursor()
    res=cur.execute("SELECT * FROM equipements")
    res=cur.fetchall()
    conn.close()
    return res
def equi_existe(num_serie):
    conn=connecter()
    cur=conn.cursor()
    cur.execute("SELECT count(*) FROM equipements WHERE num_serie= ?",(num_serie,))
    #Recupere la premiere ligne du resultat et le met dans un tuple
    res=cur.fetchone()
    conn.close()
    #[0] permet de prendre le premier element dans le tuple
    nbr=res[0]
    if nbr == 1:
        return True
    else:
        return False