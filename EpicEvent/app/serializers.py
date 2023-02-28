from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import User, Contract, Client, Event


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'role', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    @staticmethod
    def validate_phone(value):
        try:
            int(value)
            return value
        except ValueError:
            raise serializers.ValidationError('This is not a valid phone number')

    @staticmethod
    def validate_mobile(value):
        try:
            int(value)
            return value
        except ValueError:
            raise serializers.ValidationError('This is not a valid mobile number')

    def save(self):
        user_model = User
        user = user_model(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone=self.validated_data['phone'],
            mobile=self.validated_data['mobile'],
            role=self.validated_data['role'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'}
            )
        user.set_password(password)
        user.save()
        return user


class ClientListSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = ['id',
                  'email',
                  'first_name',
                  'last_name',
                  'phone',
                  'mobile',
                  'company_name',
                  'date_created',
                  'date_updated',
                  'sales_contact',
                  'status']
        read_only_fields = ('date_created', 'date_updated')

    @staticmethod
    def validate_phone(value):
        try:
            int(value)
            return value
        except ValueError:
            raise serializers.ValidationError('This is not a valid phone number')

    @staticmethod
    def validate_mobile(value):
        try:
            int(value)
            return value
        except ValueError:
            raise serializers.ValidationError('This is not a valid mobile number')

    @staticmethod
    def validate_sales_contact(value):
        if not value.role == 'sales':
            raise serializers.ValidationError('This user is not part of the sales department')
        else:
            return value


class ClientDetailSerializer(ModelSerializer):
    contracts = serializers.SerializerMethodField()
    events = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id',
                  'email',
                  'first_name',
                  'last_name',
                  'phone',
                  'mobile',
                  'company_name',
                  'date_created',
                  'date_updated',
                  'sales_contact',
                  'status',
                  'contracts',
                  'events']
        read_only_fields = ('date_created', 'date_updated')

    @staticmethod
    def get_contracts(instance):
        queryset = Contract.objects.filter(client_id=instance.id)
        serializer = ContractListSerializer(queryset, many=True)
        return serializer.data

    @staticmethod
    def get_events(instance):
        queryset = Event.objects.filter(client_id=instance.id)
        serializer = EventSerializer(queryset, many=True)
        return serializer.data


class ContractListSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ['id',
                  'date_created',
                  'date_updated',
                  'is_active',
                  'amount',
                  'payment_due',
                  'sales_contact',
                  'client']
        read_only_fields = ('date_created', 'date_updated')

    @staticmethod
    def validate_sales_contact(value):
        if not value.role == 'sales':
            raise serializers.ValidationError('This user is not part of the sales department')
        else:
            return value


class ContractDetailSerializer(ModelSerializer):
    event = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['id',
                  'date_created',
                  'date_updated',
                  'is_active',
                  'amount',
                  'payment_due',
                  'sales_contact',
                  'client',
                  'event']
        read_only_fields = ('date_created', 'date_updated')

    @staticmethod
    def get_event(instance):
        queryset = Event.objects.filter(contract_id=instance.id)
        serializer = EventSerializer(queryset, many=True)
        return serializer.data


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ['id',
                  'name',
                  'date_created',
                  'date_updated',
                  'status',
                  'attendees',
                  'event_date',
                  'notes',
                  'support_contact',
                  'client',
                  'contract']
        read_only_fields = ('date_created', 'date_updated')

    @staticmethod
    def validate_support_contact(value):
        if not value.role == 'support':
            raise serializers.ValidationError('This user is not part of the support department')
        else:
            return value

