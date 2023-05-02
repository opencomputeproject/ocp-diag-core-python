import dataclasses as dc
import re
import typing as ty

import pytest

from ocptv.output.runtime_checks import TypeCheckError, check_field_types


def test_primitive():
    @dc.dataclass
    class A:
        f1: int
        f2: str

    try:
        a = A(f1=1, f2="2")
        check_field_types(a)
    except TypeCheckError:
        pytest.fail("unexpected failed type check")

    with pytest.raises(TypeCheckError, match=re.escape("A.f1")):
        a = A(f1="1", f2="2")  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f2")):
        a = A(f1=1, f2=2)  # type: ignore
        check_field_types(a)


def test_generic_collection():
    @dc.dataclass
    class A:
        f1: ty.List[int]
        f2: ty.Dict[str, str]

    try:
        a = A(f1=[1], f2={"2": "2"})
        check_field_types(a)
    except TypeCheckError:
        pytest.fail("unexpected failed type check")

    with pytest.raises(TypeCheckError, match=re.escape("A.f1")):
        a = A(f1=["1"], f2={"2": "2"})  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f2")):
        a = A(f1=[1], f2={2: 2})  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f1")):
        a = A(f1=1, f2={"2": "2"})  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f2")):
        a = A(f1=[1], f2=2)  # type: ignore
        check_field_types(a)


def test_non_parametric_collections():
    @dc.dataclass
    class A:
        f1: ty.List
        f2: ty.Dict

    try:
        a = A(f1=[1], f2={"2": "2"})
        check_field_types(a)
    except TypeCheckError:
        pytest.fail("unexpected failed type check")


def test_generic_union():
    @dc.dataclass
    class A:
        f1: ty.Union[int, str, float]
        f2: ty.Optional[int]

    try:
        a1 = A(f1=1, f2=2)
        check_field_types(a1)

        a2 = A(f1="1", f2=None)
        check_field_types(a2)
    except TypeCheckError:
        pytest.fail("unexpected failed type check")

    with pytest.raises(TypeCheckError, match=re.escape("A.f1")):
        a = A(f1=None, f2=None)  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f2")):
        a = A(f1=1, f2="2")  # type: ignore
        check_field_types(a)


def test_generic_nested_generic():
    @dc.dataclass
    class A:
        f1: ty.Optional[ty.List[int]]
        f2: ty.Union[ty.List[int], ty.Dict[int, int]]

    try:
        a1 = A(f1=[1], f2=[2])
        check_field_types(a1)

        a2 = A(f1=None, f2={2: 2})
        check_field_types(a2)
    except TypeCheckError:
        pytest.fail("unexpected failed type check")

    with pytest.raises(TypeCheckError, match=re.escape("A.f1")):
        a = A(f1=1, f2=[1])  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f1")):
        a = A(f1=["1"], f2=[1])  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f2")):
        a = A(f1=None, f2={"2": 2})  # type: ignore
        check_field_types(a)


def test_generic_nested_object():
    @dc.dataclass
    class B:
        f1: int
        f2: ty.Optional[str] = None

    @dc.dataclass
    class A:
        f1: ty.Optional[B]
        f2: ty.List[ty.Optional[B]]

    try:
        a1 = A(f1=B(f1=1), f2=[B(f1=1)])
        check_field_types(a1)

        a2 = A(f1=None, f2=[None])
        check_field_types(a2)

        a3 = A(f1=B(f1=1, f2=None), f2=[B(f1=1, f2="2")])
        check_field_types(a3)
    except TypeCheckError:
        pytest.fail("unexpected failed type check")

    with pytest.raises(TypeCheckError, match=re.escape("A.f1")):
        a = A(f1=[B(f1=1)], f2=[None])  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f2")):
        a = A(f1=None, f2=None)  # type: ignore
        check_field_types(a)

    with pytest.raises(TypeCheckError, match=re.escape("A.f1 -> B.f1")):
        a = A(f1=B(f1="1"), f2=[None])  # type: ignore
        check_field_types(a)


def test_complex():
    @dc.dataclass
    class B:
        f1: int
        f2: ty.Optional[str] = None

    class C(dict):
        pass

    @dc.dataclass
    class A:
        f1: ty.Union[ty.Optional[B], ty.List[C], ty.Dict[int, ty.Optional[ty.List[ty.Optional[B]]]]]

    with pytest.raises(TypeCheckError, match=re.escape("A.f1 -> Dict[4] -> List[1] -> B.f2")):
        a = A(
            f1={
                1: None,
                2: [None],
                3: [B(f1=1)],
                4: [B(f1=1, f2="2"), B(f1=1, f2=2)],  # type: ignore
            }
        )
        check_field_types(a)


def test_unknown_generic_alias():
    @dc.dataclass
    class A:
        f1: ty.Callable

    with pytest.raises(ValueError, match=re.escape("unsupported")):
        a = A(f1="f1")  # type: ignore
        check_field_types(a)
