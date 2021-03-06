from typing import Any, Dict, List

class Subjects():
    subjects = [
        {
            'alias': 'fb',
            'name_en': 'fund_basis',
            'name_zh': '基金基础'
        },
        {
            'alias': 'fr',
            'name_en': 'fund_regulations',
            'name_zh': '基金法规'
        },
        {
            'alias': 'sr',
            'name_en': 'security_regulations',
            'name_zh': '证券法规'
        }
    ]

    def get_item(self, subject: str) -> Dict[str, str]:
        if subject not in self.aliases:
            raise ValueError(f'no subject named "{subject}"')
        return [i for i in self.subjects if i['alias'] == subject][0]

    @property
    def items(self) -> Any:
        return self.subjects

    @property
    def aliases(self) -> List[str]:
        return [i['alias'] for i in self.subjects]

subjects = Subjects()
