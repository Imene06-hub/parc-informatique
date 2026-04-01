from tkinter import *
from tkinter import ttk
import controlleur

# ── Palette ─────────────────────────────────────────────────────────
C_SIDEBAR_BG   = "#2D4A2D"
C_SIDEBAR_CARD = "#3A5A3A"
C_SIDEBAR_TXT  = "#FFFFFF"
C_SIDEBAR_SUB  = "#A8C4A8"
C_MAIN_BG      = "#F5F3EC"
C_TOOLBAR_BG   = "#FFFFFF"
C_BTN_GREEN    = "#3A5A3A"
C_BTN_WHITE    = "#FFFFFF"
C_BTN_WHITE_TXT= "#333333"
C_BTN_DIS      = "#E0E0E0"
C_BTN_DIS_TXT  = "#AAAAAA"
C_HEADER_BG    = "#3A5A3A"
C_HEADER_FG    = "#FFFFFF"
C_ROW_ODD      = "#FFFFFF"
C_ROW_EVEN     = "#F0EDE4"
C_SEL          = "#436FFE"
C_SEP          = "#DDDDDD"

DOT_COLORS = {
    "total":        "#AAAAAA",
    "operationnel": "#4CAF50",
    "en panne":     "#FF9800",
    "hors service": "#F44336",
    "preté":        "#2196F3",
}

# ════════════════════════════════════════════════════════════════════
def demarrer_application():
    fenetre_p = Tk()
    fenetre_p.title("Parc Informatique — Gestion des équipements")
    fenetre_p.state("zoomed")
    fenetre_p.configure(bg=C_MAIN_BG)

    # ── helpers boutons ──────────────────────────────────────────────
    def make_btn(parent, text, icon, cmd, style="white", state=NORMAL):
        """Crée un bouton stylisé. style='green' ou 'white'."""
        if state == DISABLED:
            bg, fg, abg = C_BTN_DIS, C_BTN_DIS_TXT, C_BTN_DIS
        elif style == "green":
            bg, fg, abg = C_BTN_GREEN, "white", "#2D4020"
        else:
            bg, fg, abg = C_BTN_WHITE, C_BTN_WHITE_TXT, "#E8E8E8"
        label = f"{icon}  {text}" if icon else text
        b = Button(parent, text=label, command=cmd,
                   bg=bg, fg=fg, activebackground=abg, activeforeground=fg,
                   relief="flat", font=("Segoe UI", 10), padx=12, pady=6,
                   cursor="hand2", state=state,
                   bd=0, highlightthickness=1, highlightbackground=C_SEP)
        return b

    # ════════════════════════════════════════════════════════════════
    #  PANNEAU LATÉRAL GAUCHE
    # ════════════════════════════════════════════════════════════════
    sidebar = Frame(fenetre_p, bg=C_SIDEBAR_BG, width=270)
    sidebar.pack(side=LEFT, fill=Y)
    sidebar.pack_propagate(False)

    # Logo + titre
    Frame(sidebar, bg=C_SIDEBAR_BG, height=10).pack()
    cadre_logo = Frame(sidebar, bg=C_SIDEBAR_BG)
    cadre_logo.pack(fill=X, padx=18, pady=(14, 4))

    cv_icon = Canvas(cadre_logo, width=36, height=36, bg=C_SIDEBAR_BG, highlightthickness=0)
    cv_icon.pack(side=LEFT)
    cv_icon.create_rectangle(3, 3, 33, 25, outline="white", width=2)
    cv_icon.create_rectangle(13, 25, 23, 31, fill="white", outline="white")
    cv_icon.create_line(9, 31, 27, 31, fill="white", width=2)

    cadre_titre_sb = Frame(cadre_logo, bg=C_SIDEBAR_BG)
    cadre_titre_sb.pack(side=LEFT, padx=10)
    Label(cadre_titre_sb, text="Parc Informatique",
          font=("Segoe UI", 12, "bold"), bg=C_SIDEBAR_BG, fg=C_SIDEBAR_TXT).pack(anchor=W)
    Label(cadre_titre_sb, text="Gestion des équipements",
          font=("Segoe UI", 8), bg=C_SIDEBAR_BG, fg=C_SIDEBAR_SUB).pack(anchor=W)

    Frame(sidebar, bg="#4A6A4A", height=1).pack(fill=X, padx=14, pady=10)

    # ── Statistiques ─────────────────────────────────────────────────
    Label(sidebar, text="VUE D'ENSEMBLE", font=("Segoe UI", 8, "bold"),
          bg=C_SIDEBAR_BG, fg=C_SIDEBAR_SUB).pack(anchor=W, padx=18, pady=(0, 6))

    stat_labels = {}

    def make_stat_card(key, icon_char, icon_bg, libelle):
        card = Frame(sidebar, bg=C_SIDEBAR_CARD)
        card.pack(fill=X, padx=10, pady=3)
        inner = Frame(card, bg=C_SIDEBAR_CARD)
        inner.pack(fill=X, padx=10, pady=8)

        icf = Frame(inner, bg=icon_bg, width=34, height=34)
        icf.pack(side=LEFT); icf.pack_propagate(False)
        Label(icf, text=icon_char, font=("Segoe UI", 13),
              bg=icon_bg, fg="white").place(relx=0.5, rely=0.5, anchor=CENTER)

        tf = Frame(inner, bg=C_SIDEBAR_CARD)
        tf.pack(side=LEFT, padx=8)
        Label(tf, text=libelle, font=("Segoe UI", 9),
              bg=C_SIDEBAR_CARD, fg=C_SIDEBAR_SUB).pack(anchor=W)
        lv = Label(tf, text="0", font=("Segoe UI", 15, "bold"),
                   bg=C_SIDEBAR_CARD, fg=C_SIDEBAR_TXT)
        lv.pack(anchor=W)

        dc = Canvas(inner, width=11, height=11, bg=C_SIDEBAR_CARD, highlightthickness=0)
        dc.pack(side=RIGHT, anchor=CENTER)
        dc.create_oval(1, 1, 10, 10, fill=DOT_COLORS.get(key, "#AAAAAA"), outline="")

        stat_labels[key] = lv

    make_stat_card("total",        "⬡", "#556B55", "Total")
    make_stat_card("operationnel", "▣", "#2E7D32", "Opérationnels")
    make_stat_card("en panne",     "⚠", "#7A5200", "En panne")
    make_stat_card("hors service", "⊘", "#7A1A1A", "Hors service")
    make_stat_card("preté",        "➤", "#1A4F7A", "Prêtés")

    Frame(sidebar, bg="#4A6A4A", height=1).pack(fill=X, padx=14, pady=10)

    # ── Par type ─────────────────────────────────────────────────────
    Label(sidebar, text="PAR TYPE", font=("Segoe UI", 8, "bold"),
          bg=C_SIDEBAR_BG, fg=C_SIDEBAR_SUB).pack(anchor=W, padx=18, pady=(0, 5))
    type_frame = Frame(sidebar, bg=C_SIDEBAR_BG)
    type_frame.pack(fill=X, padx=18)

    # ════════════════════════════════════════════════════════════════
    #  ZONE PRINCIPALE DROITE
    # ════════════════════════════════════════════════════════════════
    main_zone = Frame(fenetre_p, bg=C_MAIN_BG)
    main_zone.pack(side=LEFT, fill=BOTH, expand=True)

   # ── BARRE D'OUTILS (ligne 1) ─────────────────────────────────────
    toolbar = Frame(main_zone, bg=C_TOOLBAR_BG)
    toolbar.pack(fill=X)

    # 1. Bouton Ajouter (en premier, tout à gauche)
    btn_ajouter = make_btn(toolbar, "Ajouter",   "+", lambda: None, style="green")
    btn_ajouter.pack(side=LEFT, padx=(12, 4), pady=8)

    # Séparateur visuel (optionnel, pour séparer l'action d'ajout des vues)
    Frame(toolbar, bg=C_SEP, width=1).pack(side=LEFT, fill=Y, pady=6, padx=4)

    # 2. Bouton Afficher liste (en deuxième)
    btn_liste = make_btn(toolbar, "Afficher liste", "☰",
                         lambda: None, style="green")
    btn_liste.pack(side=LEFT, padx=4, pady=8)

    # 3. Bouton Trier (en troisième)
    menu_tri = Menu(fenetre_p, tearoff=0, font=("Segoe UI", 10))

    def montrer_tri():
        menu_tri.post(btn_trier.winfo_rootx(),
                      btn_trier.winfo_rooty() + btn_trier.winfo_height())

    btn_trier = Button(toolbar, text="↕  Trier par  ▾",
                       command=montrer_tri, state=DISABLED,
                       bg=C_BTN_DIS, fg=C_BTN_DIS_TXT,
                       activebackground="#E8E8E8", activeforeground=C_BTN_WHITE_TXT,
                       relief="flat", font=("Segoe UI", 10), padx=12, pady=6,
                       cursor="hand2", bd=0,
                       highlightthickness=1, highlightbackground=C_SEP)
    btn_trier.pack(side=LEFT, padx=4, pady=8)

    # -----------------------------------------------------------------
    # GESTION DU CÔTÉ DROIT (les éléments s'empilent de droite à gauche)
    # -----------------------------------------------------------------

    # 5. Bouton Supprimer (avec 80 pixels d'espace à sa droite pour l'éloigner du bord/Quitter)
    btn_suppr = make_btn(toolbar, "Supprimer", "🗑", lambda: None, state=DISABLED)
    btn_suppr.pack(side=RIGHT, padx=(4, 80), pady=8)

    # 6. Bouton Modifier (à gauche de Supprimer, il suit automatiquement le décalage)
    btn_modif = make_btn(toolbar, "Modifier",  "✎", lambda: None, state=DISABLED)
    btn_modif.pack(side=RIGHT, padx=4, pady=8)

    

    # ── BARRE DE RECHERCHE (ligne 2) ─────────────────────────────────
    search_bar = Frame(main_zone, bg="#EFEFEF", pady=6)
    search_bar.pack(fill=X)

    Label(search_bar, text="Critères :", font=("Segoe UI", 10),
          bg="#EFEFEF", fg="#555555").pack(side=LEFT, padx=(14, 4))

    combo_critere = ttk.Combobox(search_bar,
                                 values=["Tous", "Type", "Localisation",
                                         "Etat", "N° de serie"],
                                 width=13, state="readonly", font=("Segoe UI", 10))
    combo_critere.current(0)
    combo_critere.pack(side=LEFT, padx=4)

    ent_recherche = Entry(search_bar, width=36, font=("Segoe UI", 10),
                          fg="grey", relief="flat",
                          highlightthickness=1, highlightbackground=C_SEP)
    ent_recherche.pack(side=LEFT, padx=4, ipady=4)
    ent_recherche.insert(0, "Recherche...")

    def effacer_ph(event):
        if ent_recherche.get() == "Recherche...":
            ent_recherche.delete(0, END)
            ent_recherche.config(fg="black")

    def remettre_ph(event):
        if ent_recherche.get() == "":
            ent_recherche.insert(0, "Recherche...")
            ent_recherche.config(fg="grey")

    ent_recherche.bind("<FocusIn>", effacer_ph)
    ent_recherche.bind("<FocusOut>", remettre_ph)

    btn_loupe = Button(search_bar, text="🔍",
                       command=lambda: [
                           controlleur.action_rechercher(ent_recherche, combo_critere, tab),
                           rafraichir_stats()],
                       relief="flat", bg="#EFEFEF", font=("Segoe UI", 12),
                       cursor="hand2", bd=0)
    btn_loupe.pack(side=LEFT, padx=2)

    ent_recherche.bind("<Return>", lambda e: [
        controlleur.action_rechercher(ent_recherche, combo_critere, tab),
        rafraichir_stats()])

    # Séparateur
    Frame(main_zone, bg=C_SEP, height=1).pack(fill=X)

    # ── TABLEAU ───────────────────────────────────────────────────────
    cadre_tab = Frame(main_zone, bg=C_MAIN_BG)
    cadre_tab.pack(fill=BOTH, expand=True, padx=20, pady=(14, 4))

    scroll_y = Scrollbar(cadre_tab, orient=VERTICAL)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x = Scrollbar(cadre_tab, orient=HORIZONTAL)
    scroll_x.pack(side=BOTTOM, fill=X)

    colonnes = ("id", "type", "marque", "modele", "num_serie", "localisation", "etat")
    tab = ttk.Treeview(cadre_tab, columns=colonnes, show="headings",
                       yscrollcommand=scroll_y.set,
                       xscrollcommand=scroll_x.set,
                       selectmode="browse")
    scroll_y.config(command=tab.yview)
    scroll_x.config(command=tab.xview)

    headers = {
        "type": "Type", "marque": "Marque", "modele": "Modèle",
        "num_serie": "N° de Série", "localisation": "Localisation", "etat": "État"
    }
    col_widths = {"type": 120, "marque": 130, "modele": 170,
                  "num_serie": 155, "localisation": 155, "etat": 125}

    tab.column("id", width=0, stretch=NO)
    for col in ("type", "marque", "modele", "num_serie", "localisation", "etat"):
        tab.heading(col, text=headers[col])
        tab.column(col, width=col_widths[col], stretch=True, anchor=W)

    tab.pack(side=LEFT, fill=BOTH, expand=True)

    # Style tableau
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background=C_ROW_ODD, fieldbackground=C_ROW_ODD,
                    foreground="#222222", font=("Segoe UI", 10), rowheight=30)
    style.configure("Treeview.Heading",
                    background=C_HEADER_BG, foreground=C_HEADER_FG,
                    font=("Segoe UI", 10, "bold"), relief="flat")
    style.map("Treeview.Heading", background=[("active", "#2D4A2D")])
    style.map("Treeview",
              background=[("selected", C_SEL)],
              foreground=[("selected", "#111111")])
    # ── Couleurs par état (légères, lisibles) ──
    tab.tag_configure("etat_ok",      background="#E8F5E9", foreground="#1B5E20")  # vert pâle
    tab.tag_configure("etat_panne",   background="#FFF8E1", foreground="#7A5000")  # jaune pâle
    tab.tag_configure("etat_hs",      background="#FFEBEE", foreground="#7A1A1A")  # rouge pâle
    tab.tag_configure("etat_pret",    background="#E3F2FD", foreground="#0D3C6B")  # bleu pâle
    tab.tag_configure("etat_inconnu", background="#F5F5F5", foreground="#555555")  # gris neutre

    # Compteur bas
    lbl_count = Label(main_zone, text="0 équipements affichés",
                      font=("Segoe UI", 9), bg=C_MAIN_BG, fg="#888888")
    lbl_count.pack(anchor=W, padx=22, pady=(2, 8))

    # ════════════════════════════════════════════════════════════════
    #  FONCTIONS UTILITAIRES
    # ════════════════════════════════════════════════════════════════
    def rafraichir_stats():
        import model
        tous = model.afficher_tous()
        n = len(tous)
        stat_labels["total"].config(text=str(n))
        counts = {"operationnel": 0, "en panne": 0, "hors service": 0, "preté": 0}
        type_counts = {}
        for row in tous:
            ek = row[6].strip().lower()
            for k in counts:
                if ek == k:
                    counts[k] += 1
            t = row[1].strip()
            type_counts[t] = type_counts.get(t, 0) + 1
        for k, v in counts.items():
            if k in stat_labels:
                stat_labels[k].config(text=str(v))
        # PAR TYPE
        for w in type_frame.winfo_children():
            w.destroy()
        for t, cnt in sorted(type_counts.items()):
            rf = Frame(type_frame, bg=C_SIDEBAR_BG)
            rf.pack(fill=X, pady=1)
            Label(rf, text=t, font=("Segoe UI", 9),
                  bg=C_SIDEBAR_BG, fg=C_SIDEBAR_TXT).pack(side=LEFT)
            Label(rf, text=str(cnt), font=("Segoe UI", 9, "bold"),
                  bg=C_SIDEBAR_BG, fg=C_SIDEBAR_TXT).pack(side=RIGHT)
        # compteur
        visible = len(tab.get_children())
        s = "s" if visible != 1 else ""
        lbl_count.config(text=f"{visible} équipement{s} affiché{s}")

    # ── Commandes du menu Trier (ont besoin de tab + rafraichir_stats) ──
    menu_tri.add_command(label="Type",
        command=lambda: [
            controlleur.action_trierliste("type", tab),
            btn_trier.config(text="↕  Trier : Type  ▾"),
            rafraichir_stats()])
    menu_tri.add_command(label="Localisation",
        command=lambda: [
            controlleur.action_trierliste("localisation", tab),
            btn_trier.config(text="↕  Trier : Localisation  ▾"),
            rafraichir_stats()])

    # ── Brancher tous les boutons ────────────────────────────────────
    btn_liste.config(command=lambda: [
        controlleur.action_afficher_liste(tab, btn_trier),
        rafraichir_stats()])

    btn_ajouter.config(command=lambda: [
        controlleur.action_ajouter_equipement(fenetre_p, tab, btn_trier),
        rafraichir_stats()])

    btn_modif.config(command=lambda: [
        controlleur.action_modifier_equipement(fenetre_p, tab, btn_trier),
        rafraichir_stats()])

    btn_suppr.config(command=lambda: [
        controlleur.action_supprimer(tab, btn_trier),
        rafraichir_stats()])

    # ── Sélection dans le tableau ────────────────────────────────────
    tab.bind("<<TreeviewSelect>>",
             lambda e: controlleur.gerer_activation_boutons(tab, btn_modif, btn_suppr))

    def deselect_on_click(event):
        if event.widget not in (tab, btn_modif, btn_suppr):
            tab.selection_remove(tab.selection())
    fenetre_p.bind("<Button-1>", deselect_on_click)

    # ── Affichage initial ────────────────────────────────────────────
    controlleur.action_afficher_liste(tab, btn_trier)
    rafraichir_stats()

    fenetre_p.mainloop()
