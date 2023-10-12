from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Recipe, Conversation, Message
from landing.models import CustomUser
from .serializers import MessageSerializer


@api_view(['GET'])
def favorites(request):
    try:
        user = request.user
        favorites_id = [favorite.id for favorite in user.favorites.all()]
        return Response({'status': 'success', 'favorites': favorites_id})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def add_favorite(request):
    try:
        user = request.user
        recipe_id = request.data.get('recipe_id')
        user.favorites.add(recipe_id)
        return Response({'status': 'success'})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def delete_favorite(request):
    try:
        user = request.user
        recipe_id = request.data.get('recipe_id')
        user.favorites.remove(recipe_id)
        return Response({'status': 'success'})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def liked_recipes(request):
    try:
        user = request.user
        recipe_id = request.data.get('recipe_id')
        likes_id = [recipe.id for recipe in user.liked_recipes.all()]
        total = Recipe.objects.get(id=recipe_id).likes_count
        return Response({'status': 'success', 'liked_recipes': likes_id, 'total': total})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def like(request):
    try:
        user = request.user
        recipe_id = request.data.get('recipe_id')
        user.liked_recipes.add(recipe_id)

        recipe = Recipe.objects.get(id=recipe_id)
        recipe.likes_count += 1
        recipe.save()

        return Response({'status': 'success'})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def unlike(request):
    try:
        user = request.user
        recipe_id = request.data.get('recipe_id')
        user.liked_recipes.remove(recipe_id)

        recipe = Recipe.objects.get(id=recipe_id)
        if recipe.likes_count > 0:
            recipe.likes_count -= 1

        recipe.save()

        return Response({'status': 'success'})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['DELETE'])
def delete_recipe(request):
    try:
        user = request.user
        recipe_id = request.data.get('recipe_id')
        recipe = Recipe.objects.get(id=recipe_id)
        if recipe.author == user:
            recipe.delete()
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error', 'message': 'You are not the author of this recipe'})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def create_conversation(request):
    try:
        user = request.user
        participant_id = request.data.get('participant_id')

        participant = CustomUser.objects.get(id=participant_id)

        conversations = Conversation.objects.filter(
            participant1=user, participant2=participant)
        if conversations:
            return Response({'status': 'success', 'conversation_id': conversations[0].id})
        else:
            conversation = Conversation.objects.create(
                participant1=user, participant2=participant)
            return Response({'status': 'success', 'conversation_id': conversation.id})

    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['GET'])
def get_messages(request):
    try:
        user = request.user
        conversation_id = request.GET.get('conversation_id')
        conversation = Conversation.objects.get(id=conversation_id)

        messages = conversation.messages.all()
        serializer = MessageSerializer(messages, many=True)

        return Response({'status': 'success', 'messages': serializer.data})

    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})


@api_view(['POST'])
def create_message(request):
    try:
        user = request.user
        conversation_id = request.data.get('conversation_id')
        body = request.data.get('body')

        conversation = Conversation.objects.get(id=conversation_id)

        message = Message.objects.create(
            sender=user, body=body)
        conversation.messages.add(message)

        return Response({'status': 'success'})

    except Exception as e:
        return Response({'status': 'error', 'message': str(e)})