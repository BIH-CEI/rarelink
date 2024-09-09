import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from owlready2 import get_ontology, default_world
import os
from rdflib import Graph

class R2RMLMapper:
    def __init__(self, root):
        self.root = root
        self.root.title("Herramienta de Creación de Mapeos R2RML")
        self.root.configure(bg='#EFECEC')  # Fondo general
        
        self.ontology_file_path = tk.StringVar()
        self.ddl_file_path = tk.StringVar()
        
        self.setup_initial_interface()

    def setup_initial_interface(self):
        frame = tk.Frame(self.root, bg='#EFECEC')
        frame.pack(padx=10, pady=10)
        
        title_label = tk.Label(frame, text="Seleccionar Archivos", bg='#EFECEC', fg='#0C2D57', font=('Arial', 14, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        tk.Button(frame, text="Seleccionar Archivo de Ontología", command=self.load_ontology_file, bg='#FC6736', fg='white').grid(row=1, column=0, pady=5)
        tk.Entry(frame, textvariable=self.ontology_file_path, state='readonly', width=50).grid(row=1, column=1, pady=5)
        
        tk.Button(frame, text="Seleccionar Archivo DDL", command=self.load_ddl_file, bg='#FC6736', fg='white').grid(row=2, column=0, pady=5)
        tk.Entry(frame, textvariable=self.ddl_file_path, state='readonly', width=50).grid(row=2, column=1, pady=5)
        
        tk.Button(frame, text="Procesar Ontología y DDL", command=self.process_files, bg='#0C2D57', fg='white').grid(row=3, column=0, columnspan=2, pady=10)

    def load_ontology_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("OWL files", "*.owl"), ("All files", "*.*")])
        if filepath:
            self.ontology_file_path.set(filepath)
    
    def load_ddl_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("SQL files", "*.sql"), ("All files", "*.*")])
        if filepath:
            self.ddl_file_path.set(filepath)

    def process_files(self):
        ontology_path = self.ontology_file_path.get()
        ddl_path = self.ddl_file_path.get()
        
        if not ontology_path or not ddl_path:
            messagebox.showerror("Error", "Both ontology and DDL files must be selected.")
            return
        
        # Procesar Ontología
        self.ontology = get_ontology(f"file://{ontology_path}").load()
        self.ontology_classes = sorted([cls.name for cls in self.ontology.classes()])
        self.ontology_properties = {}
        self.ontology_prefixes = {}

        # Obtener prefijos de la ontología
        g = Graph()
        g.parse(ontology_path, format="xml")
        
        for prefix, namespace in g.namespaces():
            self.ontology_prefixes[prefix] = namespace

        for prop in self.ontology.properties():
            for domain in prop.domain:
                if hasattr(domain, "name"):
                    domain_name = domain.name
                    if domain_name in self.ontology_properties:
                        self.ontology_properties[domain_name].append(prop.name)
                    else:
                        self.ontology_properties[domain_name] = [prop.name]
                elif isinstance(domain, (list, set, tuple)):
                    for d in domain:
                        if hasattr(d, "name"):
                            domain_name = d.name
                            if domain_name in self.ontology_properties:
                                self.ontology_properties[domain_name].append(prop.name)
                            else:
                                self.ontology_properties[domain_name] = [prop.name]
        
        # Procesar DDL
        with open(ddl_path, 'r') as ddl_file:
            self.ddl_tables = {table: sorted(attributes) for table, attributes in self.parse_ddl(ddl_file.read()).items()}
        
        self.create_main_interface()

    def parse_ddl(self, ddl_content):
        ddl_tables = {}
        lines = ddl_content.splitlines()
        current_table = None
        for line in lines:
            line = line.strip().lower()
            if line.startswith("create table"):
                current_table = line.split()[2]
                ddl_tables[current_table] = []
            elif line and current_table and not line.startswith(");"):
                attribute = line.split()[0]
                ddl_tables[current_table].append(attribute)
        return ddl_tables

    def create_main_interface(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tk.Frame(self.root, bg='#EFECEC')
        frame.pack(padx=10, pady=10)
        
        tk.Label(frame, text="SQL Query", bg='#EFECEC', fg='#0C2D57').grid(row=0, column=0, sticky='e')
        self.sql_query_entry = tk.Entry(frame, width=100)
        self.sql_query_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(frame, text="URI del SubjectMap", bg='#EFECEC', fg='#0C2D57').grid(row=1, column=0, sticky='e')
        self.uri_entry = tk.Entry(frame, width=100)
        self.uri_entry.grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="Sujeto del SubjectMap", bg='#EFECEC', fg='#0C2D57').grid(row=2, column=0, sticky='e')
        self.subject_entry = tk.Entry(frame, width=100)
        self.subject_entry.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="Clase", bg='#EFECEC', fg='#0C2D57').grid(row=3, column=0, sticky='e')
        self.class_var = tk.StringVar()
        self.class_menu = tk.OptionMenu(frame, self.class_var, *self.ontology_classes)
        self.class_menu.configure(bg='#FFB0B0', fg='#0C2D57')
        self.class_menu.grid(row=3, column=1, pady=5)

        # Nuevo campo para seleccionar el prefijo de la ontología
        tk.Label(frame, text="Prefijo de la Clase", bg='#EFECEC', fg='#0C2D57').grid(row=4, column=0, sticky='e')
        self.prefix_var = tk.StringVar()
        self.prefix_menu = tk.OptionMenu(frame, self.prefix_var, *self.ontology_prefixes.keys())
        self.prefix_menu.configure(bg='#FFB0B0', fg='#0C2D57')
        self.prefix_menu.grid(row=4, column=1, pady=5)

        tk.Label(frame, text="Propiedades", bg='#EFECEC', fg='#0C2D57').grid(row=5, column=0, sticky='e')
        self.property_var = tk.StringVar()
        self.property_menu = tk.OptionMenu(frame, self.property_var, '')
        self.property_menu.configure(bg='#FFB0B0', fg='#0C2D57')
        self.property_menu.grid(row=5, column=1, pady=5)

        tk.Label(frame, text="Tablas", bg='#EFECEC', fg='#0C2D57').grid(row=6, column=0, sticky='e')
        self.table_var = tk.StringVar()
        self.table_menu = tk.OptionMenu(frame, self.table_var, *sorted(self.ddl_tables.keys()))
        self.table_menu.configure(bg='#FFB0B0', fg='#0C2D57')
        self.table_menu.grid(row=6, column=1, pady=5)

        tk.Label(frame, text="Atributos", bg='#EFECEC', fg='#0C2D57').grid(row=7, column=0, sticky='e')
        self.attribute_var = tk.StringVar()
        self.attribute_menu = tk.OptionMenu(frame, self.attribute_var, '')
        self.attribute_menu.configure(bg='#FFB0B0', fg='#0C2D57')
        self.attribute_menu.grid(row=7, column=1, pady=5)

        tk.Label(frame, text="Tipo de Relación", bg='#EFECEC', fg='#0C2D57').grid(row=8, column=0, sticky='e')
        self.relation_type_var = tk.StringVar()
        self.relation_type_menu = tk.OptionMenu(frame, self.relation_type_var, "rr:termType", "rr:datatype (xsd:long)", "rr:datatype (xsd:datetime)", "rr:datatype (xsd:float)", "rr:datatype (xsd:int)", "rr:datatype (xsd:string)")
        self.relation_type_menu.configure(bg='#FFB0B0', fg='#0C2D57')
        self.relation_type_menu.grid(row=8, column=1, pady=5)

        self.relations_listbox = tk.Listbox(frame, width=100, height=10, bg='#EFECEC', fg='#0C2D57')
        self.relations_listbox.grid(row=9, column=0, columnspan=2, pady=10)

        tk.Button(frame, text="Añadir Relación", command=self.add_relation, bg='#FC6736', fg='white').grid(row=10, column=0, pady=5)
        tk.Button(frame, text="Eliminar Relación", command=self.delete_relation, bg='#FC6736', fg='white').grid(row=10, column=1, pady=5)
        
        tk.Button(frame, text="Guardar Conjunto de Relaciones", command=self.save_relation_set, bg='#0C2D57', fg='white').grid(row=11, column=0, pady=10)
        tk.Button(frame, text="Exportar TTL", command=self.export_ttl, bg='#0C2D57', fg='white').grid(row=11, column=1, pady=10)

        self.block_listbox = tk.Listbox(frame, width=100, height=5, bg='#EFECEC', fg='#0C2D57')
        self.block_listbox.grid(row=12, column=0, columnspan=2, pady=10)
        self.block_listbox.bind('<Double-1>', self.load_selected_block)

        self.relation_sets = []

        self.class_var.trace('w', self.update_properties)
        self.table_var.trace('w', self.update_attributes)

    def update_properties(self, *args):
        selected_class = self.class_var.get()
        properties = sorted(self.ontology_properties.get(selected_class, []))
        self.property_menu['menu'].delete(0, 'end')
        for prop in properties:
            self.property_menu['menu'].add_command(label=prop, command=tk._setit(self.property_var, prop))

    def update_attributes(self, *args):
        selected_table = self.table_var.get()
        attributes = sorted(self.ddl_tables.get(selected_table, []))
        self.attribute_menu['menu'].delete(0, 'end')
        for attr in attributes:
            self.attribute_menu['menu'].add_command(label=attr, command=tk._setit(self.attribute_var, attr))

    def add_relation(self):
        relation_type = self.relation_type_var.get()
        property = self.property_var.get()
        attribute = self.attribute_var.get()

        if relation_type == "rr:termType":
            text_libre = simpledialog.askstring("Texto Libre", "Introduce el texto libre para la URI:")
            relation = f'rr:predicateObjectMap [ rr:predicate prefix:{property}; rr:objectMap [ rr:column "{attribute}"; rr:termType rr:IRI; rr:template "{text_libre}"; ] ]'
        elif relation_type == "rr:datatype (xsd:long)":
            relation = f'rr:predicateObjectMap [ rr:predicate prefix:{property}; rr:objectMap [ rr:column "{attribute}"; rr:datatype xsd:long; ] ]'
        elif relation_type == "rr:datatype (xsd:datetime)":
            relation = f'rr:predicateObjectMap [ rr:predicate prefix:{property}; rr:objectMap [ rr:column "{attribute}"; rr:datatype xsd:datetime; ] ]'
        elif relation_type == "rr:datatype (xsd:float)":
            relation = f'rr:predicateObjectMap [ rr:predicate prefix:{property}; rr:objectMap [ rr:column "{attribute}"; rr:datatype xsd:float; ] ]'
        elif relation_type == "rr:datatype (xsd:int)":
            relation = f'rr:predicateObjectMap [ rr:predicate prefix:{property}; rr:objectMap [ rr:column "{attribute}"; rr:datatype xsd:int; ] ]'    
        elif relation_type == "rr:datatype (xsd:string)":
            relation = f'rr:predicateObjectMap [ rr:predicate prefix:{property}; rr:objectMap [ rr:column "{attribute}"; rr:datatype xsd:string; ] ]'    
        self.relations_listbox.insert(tk.END, relation)

    def delete_relation(self):
        selected_index = self.relations_listbox.curselection()
        if selected_index:
            self.relations_listbox.delete(selected_index)

    def save_relation_set(self):
        relations = self.relations_listbox.get(0, tk.END)
        self.relation_sets.append({
            "relations": relations,
            "sql_query": self.sql_query_entry.get(),
            "uri_template": self.uri_entry.get(),
            "subject": self.subject_entry.get(),
            "selected_class": self.class_var.get(),
            "selected_prefix": self.prefix_var.get()  # Guardar el prefijo seleccionado
        })
        block_name = f"Bloque {len(self.relation_sets)}"
        self.block_listbox.insert(tk.END, block_name)
        self.relations_listbox.delete(0, tk.END)
        messagebox.showinfo("Información", f"Conjunto de relaciones guardado como {block_name}.")
        self.reset_fields()

    def reset_fields(self):
        # Resetear los desplegables
        self.class_var.set('')
        self.property_var.set('')
        self.table_var.set('')
        self.attribute_var.set('')
        self.relation_type_var.set('')
        self.sql_query_entry.delete(0, tk.END)
        self.uri_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)

    def load_selected_block(self, event):
        selected_index = self.block_listbox.curselection()
        if selected_index:
            block_index = selected_index[0]
            self.relations_listbox.delete(0, tk.END)
            for relation in self.relation_sets[block_index]["relations"]:
                self.relations_listbox.insert(tk.END, relation)

    def export_ttl(self):
        ttl_content = ""

        # Agregar prefijos
        ttl_content += "@prefix rr: <http://www.w3.org/ns/r2rml#>.\n"
        ttl_content += "@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.\n"
        for prefix, iri in self.ontology_prefixes.items():
            ttl_content += f"@prefix {prefix}: <{iri}>.\n"
        ttl_content += "\n"

        for idx, relation_set in enumerate(self.relation_sets, start=1):
            ttl_content += f"<#Bloque{idx}>\n  a rr:TriplesMap  ;\n\n"
            ttl_content += f'  rr:logicalTable [ rr:sqlQuery "{relation_set["sql_query"]}" ];\n\n'
            ttl_content += f'  rr:subjectMap [\n    rr:template "{relation_set["uri_template"]}{relation_set["subject"]}";\n    rr:class {relation_set["selected_prefix"]}:{relation_set["selected_class"]} ;\n  ];\n\n'  # Incluir el prefijo seleccionado
            for i, relation in enumerate(relation_set["relations"]):
                if i == len(relation_set["relations"]) - 1:
                    ttl_content += f"  {relation}.\n"
                else:
                    ttl_content += f"  {relation} ;\n"
            ttl_content += "\n\n"
        
        save_path = filedialog.asksaveasfilename(defaultextension=".ttl", filetypes=[("Turtle files", "*.ttl"), ("All files", "*.*")])
        if save_path:
            with open(save_path, 'w') as file:
                file.write(ttl_content)
            messagebox.showinfo("Éxito", "Archivo TTL exportado correctamente.")
        self.reset_fields()

if __name__ == "__main__":
    root = tk.Tk()
    app = R2RMLMapper(root)
    root.mainloop()
