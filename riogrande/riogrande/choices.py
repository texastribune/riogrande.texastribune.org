from djchoices import DjangoChoices, ChoiceItem


class PublicationStatus(DjangoChoices):
    Draft = ChoiceItem("D")
    Published = ChoiceItem("P")
