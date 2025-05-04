import asyncio
from typing import List
from shadai.core.schemas import Query
from shadai.core.session import Session
from src.speaker import Speaker

class ShadaiQueryRunner:
    def __init__(self, alias: str = "ariel", session_type: str = "standard", delete: bool = True, llm_max_tokens: int = 500):
        self.alias = alias
        self.session_type = session_type
        self.delete = delete
        self.llm_max_tokens = llm_max_tokens
        self.speaker = Speaker()

    async def get_response(self, query_text: str) -> str:
        # Crear la consulta basada en el texto proporcionado
        queries: List[Query] = [
            Query(
                query=query_text,
                role="Eres un asistente especializado en asistencia a personas con discapacidad,tienes responde con maximo 1 parrafos de 4 reglones sin comillas ni caracteres especiales",
                display_in_console=True,
            ),
        ]
        
        # Ejecutar la consulta
        async with Session(
            alias=self.alias,
            type=self.session_type,
            delete=self.delete,
            llm_max_tokens=self.llm_max_tokens
        ) as session:
            response = await session.multiple_queries(queries=queries)
        
        
        # Retornar la respuesta (asumimos que la respuesta es un string)
        if response:
            self.speaker.speak(response[0].response)
            return response
        else:
            return "No se obtuvo respuesta"


    def query(self, query_text: str):
        return asyncio.run(self.get_response(query_text))

if __name__ == "__main__":
    runner = ShadaiQueryRunner()
    response = runner.query("me siento solo")
    print(response)
