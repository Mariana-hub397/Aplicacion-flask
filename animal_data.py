class Animal:
    def __init__(self, animal_id, alimentacion, salud, comportamiento, manejo_ambiental, fecha):
        self.animal_id = animal_id
        self.alimentacion = alimentacion
        self.salud = salud
        self.comportamiento = comportamiento
        self.manejo_ambiental = manejo_ambiental
        self.fecha = fecha

    def formato_doc(self):
        return {
            'animal_id': self.animal_id,
            'alimentacion': self.alimentacion,
            'salud': self.salud,
            'comportamiento': self.comportamiento,
            'manejo_ambiental': self.manejo_ambiental,
            'fecha': self.fecha
        }

