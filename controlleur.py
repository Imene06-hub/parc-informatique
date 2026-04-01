import model
from tkinter import messagebox, ttk
from tkinter import *

# ── Palette partagée ───────────────────────────────────────────────
C_GREEN_DARK = "#2D4A2D"
C_BTN_BG     = "#3A5A3A"
C_BTN_FG     = "#FFFFFF"
C_BTN_ABG    = "#2D4020"
C_BG_MAIN    = "#F5F3EC"
C_SEP        = "#DDDDDD"
C_RED        = "#C0392B"
C_BTN_DIS    = "#E0E0E0"
C_BTN_DIS_TXT= "#AAAAAA"

# ── Tags couleur selon l'état ──────────────────────────────────────
# Ces tags doivent correspondre à ceux configurés dans vue.py
ETAT_TAG = {
    "operationnel": "etat_ok",
    "en panne":     "etat_panne",
    "hors service": "etat_hs",
    "preté":        "etat_pret",
}

def _tag_etat(etat):
    return ETAT_TAG.get(etat.strip().lower(), "etat_inconnu")

def _inserer_lignes(tab, donnees):
    """Insère les lignes avec le bon tag couleur selon l'état."""
    for ligne in donnees:
        etat = ligne[6] if len(ligne) > 6 else ""
        tab.insert('', 'end', values=ligne, tags=(_tag_etat(etat),))

# ── Helpers popup ──────────────────────────────────────────────────
def _style_popup(f):
    f.configure(bg=C_BG_MAIN)

def _bandeau(f, texte):
    fr = Frame(f, bg=C_GREEN_DARK)
    fr.pack(side=TOP, fill=X)
    Label(fr, text=texte, font=("Segoe UI", 12, "bold"),
          bg=C_GREEN_DARK, fg="white", anchor=W, padx=20, pady=12).pack(fill=X)

def _lbl(cadre, texte, row):
    Label(cadre, text=texte, width=14, anchor="e",
          bg=C_BG_MAIN, font=("Segoe UI", 10), fg="#333333").grid(
        row=row, column=0, pady=7, padx=(10, 0), sticky=E)

def _btn_popup(parent, texte, cmd, style="primary"):
    if style == "primary":
        bg, fg, abg = C_BTN_BG, C_BTN_FG, C_BTN_ABG
    else:
        bg, fg, abg = "#FFFFFF", "#333333", "#E8E8E8"
    return Button(parent, text=texte, command=cmd,
                  bg=bg, fg=fg, activebackground=abg, activeforeground=fg,
                  font=("Segoe UI", 10), relief="flat", padx=16, pady=7,
                  cursor="hand2", bd=0,
                  highlightthickness=1, highlightbackground=C_SEP)

# ══════════════════════════════════════════════════════════════════
#  AFFICHER / TRIER
# ══════════════════════════════════════════════════════════════════
def action_afficher_liste(tab, btn_trier):
    donnee = model.afficher_tous()
    for item in tab.get_children():
        tab.delete(item)
    _inserer_lignes(tab, donnee)
    btn_trier.config(state=NORMAL, bg="#FFFFFF", fg="#333333")

def action_trierliste(critere, tab):
    donnee = model.trier(critere)
    for item in tab.get_children():
        tab.delete(item)
    _inserer_lignes(tab, donnee)

# ══════════════════════════════════════════════════════════════════
#  AJOUTER
# ══════════════════════════════════════════════════════════════════
def action_ajouter_equipement(fenetre_p, tab, btn_trier):
    fa = Toplevel(fenetre_p)
    fa.title("Ajouter un équipement")
    fa.geometry("450x430")
    fa.resizable(False, False)
    fa.transient(fenetre_p)
    fa.grab_set()
    _style_popup(fa)
    _bandeau(fa, "Ajouter un équipement")

    cadre = Frame(fa, bg=C_BG_MAIN)
    cadre.pack(padx=5, pady=10)

    for i, c in enumerate(["Type", "Marque", "Modèle", "N° de série", "Localisation", "État"]):
        _lbl(cadre, c, i)
        

    w_type = ttk.Combobox(cadre, values=["PC", "Portable", "Imprimante", "Routeur", "Ecran"],
                          width=21, font=("Segoe UI", 10))
    w_type.grid(row=0, column=2, padx=12, pady=7, sticky=W)

    def entry_ph(row, ph):
        e = Entry(cadre, width=23, font=("Segoe UI", 10), fg="grey",
                  relief="flat", highlightthickness=1, highlightbackground=C_SEP)
        e.grid(row=row, column=2, padx=12, pady=7, sticky=W)
        e.insert(0, ph)
        e.bind("<FocusIn>",  lambda ev, _e=e, _p=ph: (_e.delete(0, END), _e.config(fg="black")) if _e.get() == _p else None)
        e.bind("<FocusOut>", lambda ev, _e=e, _p=ph: (_e.insert(0, _p), _e.config(fg="grey")) if _e.get() == "" else None)
        return e

    w_marque    = entry_ph(1, "Ex : Dell, HP, Apple…")
    w_modele    = entry_ph(2, "Ex : MacBook Air, XPS 13…")
    w_num_serie = entry_ph(3, "Ex : 123456ABC")

    w_loc = ttk.Combobox(cadre, values=["Bureau", "Salle", "Batiment"],
                         width=21, font=("Segoe UI", 10))
    w_loc.grid(row=4, column=2, padx=12, pady=7, sticky=W)

    w_etat = ttk.Combobox(cadre, values=["Operationnel", "En panne", "Hors Service", "Preté"],
                          width=21, font=("Segoe UI", 10))
    w_etat.grid(row=5, column=2, padx=12, pady=7, sticky=W)

    Label(cadre, text="Tous les champs sont obligatoires", fg=C_RED, font=("Segoe UI", 9, "bold"),
          bg=C_BG_MAIN).grid(row=6, column=0, columnspan=3, pady=(10, 0))

    cadre_b = Frame(fa, bg=C_BG_MAIN)
    cadre_b.pack(side=BOTTOM, pady=12)

    def reinit():
        w_type.set('')
        for e, ph in [(w_marque, "Ex : Dell, HP, Apple…"),
                      (w_modele, "Ex : MacBook Air, XPS 13…"),
                      (w_num_serie, "Ex : 123456ABC")]:
            e.delete(0, END); e.insert(0, ph); e.config(fg="grey")
        w_loc.set(''); w_etat.set('')

    _btn_popup(cadre_b, "Effacer", reinit, style="secondary").pack(side=LEFT, padx=6)
    _btn_popup(cadre_b, "Ajouter",
               lambda: valider_ajout(w_type, w_marque, w_modele, w_num_serie,
                                     w_loc, w_etat, fa, tab, btn_trier)
               ).pack(side=LEFT, padx=6)


def valider_ajout(type_, marque, modele, num_serie, localisation, etat, fa, tab, btn_trier):
    t = type_.get(); ma = marque.get(); mo = modele.get()
    num = num_serie.get(); l = localisation.get(); e = etat.get()
    phs = {"Ex : Dell, HP, Apple…", "Ex : MacBook Air, XPS 13…", "Ex : 123456ABC"}
    if not t or not ma or not mo or not num or not l or not e or ma in phs or mo in phs or num in phs:
        messagebox.showwarning("Champs vides", "Tous les champs sont obligatoires.")
        return
    if model.equi_existe(num):
        messagebox.showerror("Erreur", "Un équipement avec ce numéro de série existe déjà.")
        return
    model.ajouter_equipement(t, ma, mo, num, l, e)
    messagebox.showinfo("Succès", "Équipement ajouté avec succès.")
    action_afficher_liste(tab, btn_trier)
    fa.destroy()

# ══════════════════════════════════════════════════════════════════
#  MODIFIER
# ══════════════════════════════════════════════════════════════════
def action_modifier_equipement(fenetre_p, tab, btn_trier):
    selection = tab.selection()
    if not selection:
        messagebox.showwarning("Aucune sélection", "Veuillez sélectionner un équipement.")
        return
    valeurs = tab.item(selection[0], "values")
    id_equip = valeurs[0]
    type_, marque, modele, num_serie, localisation, etat = valeurs[1:]

    fm = Toplevel(fenetre_p)
    fm.title("Modifier un équipement")
    fm.geometry("450x430")
    fm.resizable(False, False)
    fm.transient(fenetre_p)
    fm.grab_set()
    _style_popup(fm)
    _bandeau(fm, "Modifier un équipement")

    cadre = Frame(fm, bg=C_BG_MAIN)
    cadre.pack(padx=5, pady=10)

    for i, c in enumerate(["Type", "Marque", "Modèle", "N° de série", "Localisation", "État"]):
        _lbl(cadre, c, i)
        

    w_type = ttk.Combobox(cadre, values=["PC", "Portable", "Imprimante", "Routeur", "Ecran"],
                          width=21, font=("Segoe UI", 10))
    w_type.grid(row=0, column=2, padx=12, pady=7, sticky=W)
    w_type.set(type_)

    def entry_val(row, val):
        e = Entry(cadre, width=23, font=("Segoe UI", 10),
                  relief="flat", highlightthickness=1, highlightbackground=C_SEP)
        e.grid(row=row, column=2, padx=12, pady=7, sticky=W)
        e.insert(0, val)
        return e

    w_marque    = entry_val(1, marque)
    w_modele    = entry_val(2, modele)
    w_num_serie = entry_val(3, num_serie)

    w_loc = ttk.Combobox(cadre, values=["Bureau", "Salle", "Batiment"],
                         width=21, font=("Segoe UI", 10))
    w_loc.grid(row=4, column=2, padx=12, pady=7, sticky=W)
    w_loc.set(localisation)

    w_etat = ttk.Combobox(cadre, values=["Operationnel", "En panne", "Hors Service", "Preté"],
                          width=21, font=("Segoe UI", 10))
    w_etat.grid(row=5, column=2, padx=12, pady=7, sticky=W)
    w_etat.set(etat)

    Label(cadre, text="Tous les champs sont obligatoires", fg=C_RED, font=("Segoe UI", 9, "bold"),
          bg=C_BG_MAIN).grid(row=6, column=0, columnspan=3, pady=(10, 0))

    cadre_b = Frame(fm, bg=C_BG_MAIN)
    cadre_b.pack(side=BOTTOM, pady=12)

    def reinit():
        w_type.set(type_)
        for e, v in [(w_marque, marque), (w_modele, modele), (w_num_serie, num_serie)]:
            e.delete(0, END); e.insert(0, v)
        w_loc.set(localisation); w_etat.set(etat)

    _btn_popup(cadre_b, "Réinitialiser", reinit, style="secondary").pack(side=LEFT, padx=6)
    _btn_popup(cadre_b, "Valider",
               lambda: valider_modification(id_equip, num_serie, w_type, w_marque,
                                            w_modele, w_num_serie, w_loc, w_etat,
                                            fm, tab, btn_trier)
               ).pack(side=LEFT, padx=6)


def valider_modification(id_equip, num_origine, type_, marque, modele, w_num,
                         localisation, etat, fm, tab, btn_trier):
    t = type_.get(); ma = marque.get(); mo = modele.get()
    n = w_num.get(); l = localisation.get(); e = etat.get()
    if not t or not ma or not mo or not n or not l or not e:
        messagebox.showwarning("Erreur", "Tous les champs sont obligatoires.")
        return
    if n != num_origine and model.equi_existe(n):
        messagebox.showerror("Erreur", "Ce numéro de série est déjà utilisé.")
        return
    model.modifier_equipement(id_equip, t, ma, mo, n, l, e)
    messagebox.showinfo("Succès", "Équipement modifié avec succès.")
    action_afficher_liste(tab, btn_trier)
    fm.destroy()

# ══════════════════════════════════════════════════════════════════
#  SUPPRIMER
# ══════════════════════════════════════════════════════════════════
def action_supprimer(tab, btn_trier):
    selection = tab.selection()
    num_serie = tab.set(selection, "num_serie")
    rep = messagebox.askyesno("Suppression",
                              f"Voulez-vous supprimer l'équipement n° {num_serie} ?")
    if rep:
        model.supprimer_equipement(num_serie)
        action_afficher_liste(tab, btn_trier)
        messagebox.showinfo("Succès", "Équipement supprimé avec succès.")

# ══════════════════════════════════════════════════════════════════
#  RECHERCHE
# ══════════════════════════════════════════════════════════════════
def action_rechercher(texte, critere, tab):
    t = texte.get()
    c = critere.get()
    if t in ("Recherche...", "") or c == "Tous":
        val = "" if t == "Recherche..." else t
        res = model.recherche_generique(val)
    else:
        mapping = {
            "Type": "type",
            "Localisation": "localisation",
            "Etat": "etat",
            "N° de serie": "num_serie",
        }
        col = mapping.get(c, c.lower())
        res = model.rechercher_equipement(col, t)
    for item in tab.get_children():
        tab.delete(item)
    _inserer_lignes(tab, res)

# ══════════════════════════════════════════════════════════════════
#  GESTION BOUTONS
# ══════════════════════════════════════════════════════════════════
def gerer_activation_boutons(tableau, b_modif, b_suppr):
    if tableau.selection():
        b_modif.config(state=NORMAL, bg="#3A5A3A", fg="white",
                       highlightbackground="#3A5A3A")
        b_suppr.config(state=NORMAL, bg="#3A5A3A", fg="white",
                       highlightbackground="#3A5A3A")
    else:
        b_modif.config(state=DISABLED, bg=C_BTN_DIS, fg=C_BTN_DIS_TXT,
                       highlightbackground=C_BTN_DIS)
        b_suppr.config(state=DISABLED, bg=C_BTN_DIS, fg=C_BTN_DIS_TXT,
                       highlightbackground=C_BTN_DIS)
