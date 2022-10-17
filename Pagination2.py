import math

class Pagination():
    def __init__(self, items = [], page_size=10):
        self.items = items
        self.page_size = page_size
        self.current_page = self.items[:self.page_size]
        self.current_count = self.page_size
        self.number_of_pages = math.ceil(len(items)/page_size)
        self.current_number_of_page = 1

    def get_visible_items(self):
        return self.current_page

    def prev_page(self):
        return self.go_to_page(self, self.current_number_of_page-1)

    def next_page(self):
        self.current_page = self.items[self.current_count :
        self.current_count + self.page_size]
        if self.current_page != []:
            self.current_count += self.page_size
        return self.current_page

    def first_page(self):
        self.current_page = self.items[:self.page_size]
        self.current_count = self.page_size
        return self.current_page

    def last_page(self):
        if len(self.items)%self.page_size != 0:
            self.current_page = self.items[-((len(self.items))%self.page_size):]
            self.current_count = len(self.items) + self.page_size - len(self.items)%self.page_size
        else:
            self.current_page = self.items[-self.page_size:]
            self.current_count = len(self.items)
        return self.current_page

    def go_to_page(self, number_of_size):
        if number_of_size > self.number_of_pages:
            print('Такой страницы не существует')
            return []
        else:
            i = 1
            self.current_count = 0
            while i < number_of_size:
                self.current_count += self.page_size
                i+=1
            self.current_page = self.items[self.current_count:self.current_count+self.page_size]
            self.current_number_of_page = number_of_size
            return self.current_page



number_one = Pagination([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 6)





print ('текущая ',number_one.get_visible_items())
print ('предыдущая ',number_one.prev_page())
print ('следующая ',number_one.next_page())
print ('следующая ',number_one.next_page())
print ('четвертая',number_one.go_to_page(4))
print ('первая',number_one.first_page())
print ('предыдущая ',number_one.prev_page())
print ('последняя ',number_one.last_page())
print ('следующая ',number_one.next_page())
print ('предыдущая ',number_one.prev_page())
print ('предыдущая ',number_one.prev_page())
print ('следующая ',number_one.next_page())
print ('текущая ',number_one.get_visible_items())
print ('первая' ,number_one.go_to_page(1))
