from typing import Any
from sqlalchemy.orm import mapped_column, DeclarativeBase, relationship
from sqlalchemy import Column,Integer, String, DateTime, func, BigInteger, Float, ForeignKey, Date
class Base(DeclarativeBase):
    pass
class Subfolder(Base):
    __tablename__ = 'Subfolders'

    SubfolderID = Column(Integer, primary_key=True, autoincrement=True)
    SubfolderName = Column(String(255), nullable=False)

    files = relationship('File', back_populates='subfolder')


class Project(Base):
    __tablename__ = 'Projects'

    ProjectID = Column(Integer, primary_key=True, autoincrement=True)
    ProjectName = Column(String(255), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date)

    files = relationship('File', back_populates='project')


class File(Base):
    __tablename__ = 'Files'

    FileID = Column(Integer, primary_key=True, autoincrement=True)
    FileName = Column(String(255), nullable=False)
    FilePath = Column(String(255), nullable=False)
    FileType = Column(String(50), nullable=False)
    SubfolderID = Column(Integer, ForeignKey('Subfolders.SubfolderID', ondelete='CASCADE'))
    ProjectID = Column(Integer, ForeignKey('Projects.ProjectID', ondelete='CASCADE'))

    subfolder = relationship('Subfolder', back_populates='files')
    project = relationship('Project', back_populates='files')
    tags = relationship('FileTag', back_populates='file')


class Tag(Base):
    __tablename__ = 'Tags'

    TagID = Column(Integer, primary_key=True, autoincrement=True)
    TagName = Column(String(255), nullable=False)

    file_tags = relationship('FileTag', back_populates='tag')


class FileTag(Base):
    __tablename__ = 'FileTags'

    FileTagID = Column(Integer, primary_key=True, autoincrement=True)
    FileID = Column(Integer, ForeignKey('Files.FileID', ondelete='CASCADE'))
    TagID = Column(Integer, ForeignKey('Tags.TagID', ondelete='CASCADE'))

    file = relationship('File', back_populates='tags')
    tag = relationship('Tag', back_populates='file_tags')
