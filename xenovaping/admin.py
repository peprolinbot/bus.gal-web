from django.contrib import admin
from django.db import models
from django.forms import NumberInput

from admin_extra_buttons.api import ExtraButtonsMixin, button

from .utils.notifications import notify_email as notify_pending_refund
from .utils.notifications import run_checks as run_notification_checks
from .utils.account import account

from .models import Card, Owner


class CardAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ["number", "owner", "last_pending"]
    ordering = ["last_pending"]
    actions = ["reset_card", "send_pending_refund_email", "pull_card_pending"]

    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size': '20'})},
    }

    @admin.action(description="Reset selected cards to 0 pending")
    def reset_card(self, request, queryset):
        queryset.update(last_pending=0)

    @admin.action(description="Send 'pending refund' email for the selected cards")
    def send_pending_refund_email(self, request, queryset):
        for card in queryset:
            notify_pending_refund(
                card.owner.email, card.number, card.last_pending)

    @admin.action(description="Pull the latest 'pending' values for the selected cards")
    def pull_card_pending(self, request, queryset):
        for card in queryset:
            card.last_pending = account.get_card(card.number).pending
            card.save()

    @button(html_attrs={'style': 'background-color:#88FF88;color:black'})
    def force_run_of_the_notification_checks(self, request):
        notified_cards = run_notification_checks()
        self.message_user(request, f"Notified {len(notified_cards)} cards: {', '.join([str(c.number) for c in notified_cards])}")


class CardInline(admin.TabularInline):
    model = Card
    extra = 0

    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size': '20'})},
    }


class OwnerAdmin(admin.ModelAdmin):
    list_display = ["email"]
    ordering = ["email"]
    inlines = [CardInline]


admin.site.register(Card, CardAdmin)
admin.site.register(Owner, OwnerAdmin)
