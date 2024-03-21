
CREATE TABLE Teaterstykke (
    StykkeID int PRIMARY KEY,
    StykkeNavn varchar(255) NOT NULL,
    Forfatter varchar(255),
    Sesong varchar(255) NOT NULL
);

CREATE TABLE StykkeiSal (
    StykkeID int,
    TeaterSalID int,
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID),
    FOREIGN KEY (TeaterSalID) REFERENCES Teatersal(TeaterSalID),
    PRIMARY KEY (StykkeID, TeaterSalID)
);

CREATE TABLE Teatersal (
    TeaterSalID int PRIMARY KEY,
    TeaterSalNavn varchar(255) NOT NULL,
    Plasser int NOT NULL
);

CREATE TABLE Forestilling (
    ForestillingID int PRIMARY KEY,
    Dato date NOT NULL,
    Tid time NOT NULL,
    TeaterSalID int NOT NULL,
    FOREIGN KEY (TeaterSalID) REFERENCES Teatersal(TeaterSalID)
);

CREATE TABLE Billett (
    BillettNummer int PRIMARY KEY,
    KundeType varchar(255) NOT NULL,
    Pris int NOT NULL,
    Dato date NOT NULL,
    ForestillingID int NOT NULL,
    StolID int NOT NULL,
    FOREIGN KEY (ForestillingID) REFERENCES Forestilling(ForestillingID),
    FOREIGN KEY (StolID) REFERENCES Stol(StolID)
);

CREATE TABLE Stol (
    StolID int PRIMARY KEY,
    SeteNr int NOT NULL,
    RadNr int NOT NULL,
    Omraadet varchar(255) NOT NULL,
    TeaterSalID int NOT NULL,
    FOREIGN KEY (TeaterSalID) REFERENCES Teatersal(TeaterSalID)
);

CREATE TABLE Kunde (
    KundeNummer int PRIMARY KEY,
    Mobilnummer int NOT NULL,
    Navn varchar(255) NOT NULL,
    Addresse varchar(255) NOT NULL
);

CREATE TABLE Akt (
    AktID int PRIMARY KEY,
    Aktnummer int NOT NULL,
    Aktnavn varchar(255),
    StykkeID int NOT NULL,
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
);

CREATE TABLE RolleiAkt (
    AktID int,
    RolleID int,
    FOREIGN KEY (AktID) REFERENCES Akt(AktID),
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID),
    PRIMARY KEY (AktID, RolleID)
);

CREATE TABLE Rolle (
    RolleID int PRIMARY KEY,
    RolleNavn varchar(255) NOT NULL
);

CREATE TABLE SkuespilleriRolle (
    RolleID int,
    SkuespillerID int,
    FOREIGN KEY (RolleID) REFERENCES Rolle(RolleID),
    FOREIGN KEY (SkuespillerID) REFERENCES Skuespiller(SkuespillerID)
);

CREATE TABLE Skuespiller (
    SkuespillerID int PRIMARY KEY,
    Navn varchar(255) NOT NULL,
    Epost varchar(255) NOT NULL,
    Telefonnummer int 
);

CREATE TABLE Oppgave (
    OppgaveID int PRIMARY KEY,
    OppgaveNavn varchar(255) NOT NULL,
    StykkeID int NOT NULL,
    FOREIGN KEY (StykkeID) REFERENCES Teaterstykke(StykkeID)
);

CREATE TABLE AnsattiOppgave (
    OppgaveID int,
    AnsattID int,
    FOREIGN KEY (OppgaveID) REFERENCES Oppgave(OppgaveID),
    FOREIGN KEY (AnsattID) REFERENCES Ansatt(AnsattID),
    PRIMARY KEY (OppgaveID, AnsattID)
);

CREATE TABLE Ansatt (
    AnsattID int PRIMARY KEY,
    Navn varchar(255) NOT NULL,
    Epost varchar(255) NOT NULL,
    AnsattStatus varchar(255) NOT NULL
);